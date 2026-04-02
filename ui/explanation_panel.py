import pygame
from core.constants import (
    C_PANEL2, C_BORDER, C_CYAN, C_GREEN, C_ORANGE, C_PURPLE, C_YELLOW, C_RED,
    C_TEXT, C_TEXT_DIM, C_TEXT_MUTED,
    EXPL_X, CANVAS_TOP, EXPL_W, CANVAS_H,
)

COMPLEXITY = {
    "Bubble Sort":    ("O(n)",       "O(n²)",      "O(n²)",      "O(1)"),
    "Selection Sort": ("O(n²)",      "O(n²)",      "O(n²)",      "O(1)"),
    "Merge Sort":     ("O(n log n)", "O(n log n)", "O(n log n)", "O(n)"),
    "BFS":            ("O(V+E)",     "O(V+E)",     "O(V+E)",     "O(V)"),
    "Dijkstra":       ("O(E log V)", "O(E log V)", "O(E log V)", "O(V)"),
}

ALGO_DESC = {
    "Bubble Sort":    "Repeatedly compares adjacent elements and swaps them if out of order. Simple but slow for large inputs.",
    "Selection Sort": "Finds the minimum element each pass and places it at the front. Always O(n2) regardless of input.",
    "Merge Sort":     "Divides array in half recursively then merges sorted halves. Guaranteed O(n log n) performance.",
    "BFS":            "Explores all neighbours level by level using a queue. Guarantees shortest path on unweighted grids.",
    "Dijkstra":       "Uses a priority queue to always expand the lowest-cost node. Finds shortest path on weighted graphs.",
}

MAX_LOG = 14


class ExplanationPanel:
    def __init__(self, state):
        self.state     = state
        self.step_log  = []
        self.cur_step  = 0
        self.total_steps = 0

        pygame.font.init()
        self.f_title = pygame.font.SysFont("Consolas", 13, bold=True)
        self.f_body  = pygame.font.SysFont("Consolas", 12)
        self.f_sm    = pygame.font.SysFont("Consolas", 11)
        self.f_step  = pygame.font.SysFont("Consolas", 12)

    def reset(self):
        self.step_log    = []
        self.cur_step    = 0
        self.total_steps = 0

    def push_step(self, text):
        self.cur_step += 1
        self.step_log.append(f"[{self.cur_step:03d}] {text}")
        if len(self.step_log) > MAX_LOG:
            self.step_log.pop(0)

    # ─────────────────────────────────────────────────────────────────────────
    def draw(self, surface):
        pygame.draw.rect(surface, C_PANEL2,
                         pygame.Rect(EXPL_X, CANVAS_TOP, EXPL_W, CANVAS_H))
        pygame.draw.line(surface, C_BORDER,
                         (EXPL_X, CANVAS_TOP), (EXPL_X, CANVAS_TOP + CANVAS_H))

        # Header
        hh = 36
        pygame.draw.rect(surface, (12, 18, 32),
                         pygame.Rect(EXPL_X, CANVAS_TOP, EXPL_W, hh))
        pygame.draw.line(surface, C_BORDER,
                         (EXPL_X, CANVAS_TOP + hh), (EXPL_X + EXPL_W, CANVAS_TOP + hh))
        pygame.draw.circle(surface, C_ORANGE, (EXPL_X + 14, CANVAS_TOP + hh // 2), 5)
        lbl = self.f_title.render("EXPLANATION", True, C_TEXT_DIM)
        surface.blit(lbl, (EXPL_X + 28, CANVAS_TOP + hh // 2 - lbl.get_height() // 2))

        y   = CANVAS_TOP + hh + 12
        pad = EXPL_X + 12

        # Step counter
        sc = self.f_sm.render(f"STEP  {self.cur_step} / {self.total_steps}", True, C_TEXT_MUTED)
        surface.blit(sc, (pad, y)); y += 20

        # Current step message (word-wrapped)
        msg = self.state.status_msg or "Press Start to begin."
        for line in self._wrap(msg, EXPL_W - 24):
            s = self.f_step.render(line, True, C_TEXT)
            surface.blit(s, (pad, y)); y += 17
        y += 8

        # ── About ─────────────────────────────────────────────────────────────
        self._divider(surface, y); y += 14
        al = self.f_sm.render("ABOUT", True, C_TEXT_MUTED)
        surface.blit(al, (pad, y)); y += 16
        desc = ALGO_DESC.get(self.state.algo_name, "")
        for line in self._wrap(desc, EXPL_W - 24):
            s = self.f_sm.render(line, True, C_TEXT_DIM)
            surface.blit(s, (pad, y)); y += 14
        y += 8

        # ── Complexity ────────────────────────────────────────────────────────
        self._divider(surface, y); y += 14
        cl = self.f_sm.render("COMPLEXITY", True, C_TEXT_MUTED)
        surface.blit(cl, (pad, y)); y += 16
        cx = COMPLEXITY.get(self.state.algo_name, ("—", "—", "—", "—"))
        for label, val, col in [("Best", cx[0], C_GREEN), ("Average", cx[1], C_YELLOW),
                                  ("Worst", cx[2], C_RED), ("Space", cx[3], C_PURPLE)]:
            ls = self.f_sm.render(label + ":", True, C_TEXT_MUTED)
            vs = self.f_sm.render(val, True, col)
            surface.blit(ls, (pad, y))
            surface.blit(vs, (EXPL_X + EXPL_W - vs.get_width() - 12, y))
            y += 17
        y += 8

        # ── Live stats ────────────────────────────────────────────────────────
        self._divider(surface, y); y += 14
        stl = self.f_sm.render("LIVE STATS", True, C_TEXT_MUTED)
        surface.blit(stl, (pad, y)); y += 16
        if self.state.mode == "sorting":
            rows = [("Comparisons", str(self.state.comparisons), C_CYAN),
                    ("Swaps",       str(self.state.swaps),       C_ORANGE)]
        else:
            rows = [("Visited",     str(self.state.nodes_visited), C_CYAN),
                    ("Path length", str(self.state.path_length),   C_GREEN)]
        for label, val, col in rows:
            ls = self.f_sm.render(label + ":", True, C_TEXT_MUTED)
            vs = self.f_body.render(val, True, col)
            surface.blit(ls, (pad, y))
            surface.blit(vs, (EXPL_X + EXPL_W - vs.get_width() - 12, y))
            y += 17
        y += 8

        # ── Step log ──────────────────────────────────────────────────────────
        if y + 40 < CANVAS_TOP + CANVAS_H:
            self._divider(surface, y); y += 14
            ll = self.f_sm.render("STEP LOG", True, C_TEXT_MUTED)
            surface.blit(ll, (pad, y)); y += 16
            for entry in self.step_log[-MAX_LOG:]:
                if y + 13 > CANVAS_TOP + CANVAS_H - 6:
                    break
                es = self.f_sm.render(entry[:33], True, C_TEXT_MUTED)
                surface.blit(es, (pad, y)); y += 13

    def _divider(self, surface, y):
        pygame.draw.line(surface, C_BORDER,
                         (EXPL_X + 8, y), (EXPL_X + EXPL_W - 8, y), 1)

    def _wrap(self, text, max_w):
        words, lines, cur = text.split(), [], ""
        for w in words:
            test = (cur + " " + w).strip()
            if self.f_sm.size(test)[0] > max_w and cur:
                lines.append(cur); cur = w
            else:
                cur = test
        if cur: lines.append(cur)
        return lines
