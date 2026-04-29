import pygame
from core.constants import (
    C_BG, C_BORDER, C_TEXT_MUTED, C_TEXT_DIM,
    C_BAR_DEFAULT, C_BAR_ACTIVE, C_BAR_COMPARED,
    C_BAR_SWAP, C_BAR_SORTED, C_BAR_PIVOT,
    CANVAS_TOP, CANVAS_H, VIZ_X, VIZ_W,
    BAR_PADDING, BAR_AREA_MARGIN,
)

# ── Bar colours (unchanged) ───────────────────────────────────────────────────
COLOUR_MAP = {
    "default":  C_BAR_DEFAULT,
    "active":   C_BAR_ACTIVE,
    "compared": C_BAR_COMPARED,
    "swap":     C_BAR_SWAP,
    "sorted":   C_BAR_SORTED,
    "pivot":    C_BAR_PIVOT,
}

# ── Footer box colours ────────────────────────────────────────────────────────
# Blue = idle/default, Red = active/comparing/swapping, Green = sorted/done
FOOTER_BOX_BG = {
    "default":  (20,  60, 140),    # blue
    "active":   (180, 30,  50),    # red
    "compared": (160, 25,  45),    # red (slightly different shade)
    "swap":     (200, 35,  35),    # red-orange
    "sorted":   (20, 140,  60),    # green
    "pivot":    (160, 110,  10),   # gold (for quick sort pivot)
}
FOOTER_BOX_BORDER = {
    "default":  (50,  100, 200),
    "active":   (255,  60,  80),
    "compared": (230,  50,  70),
    "swap":     (255,  70,  50),
    "sorted":   (50,  210,  90),
    "pivot":    (220, 170,  30),
}
FOOTER_TEXT = {
    "default":  (140, 190, 255),
    "active":   (255, 255, 255),
    "compared": (255, 240, 240),
    "swap":     (255, 255, 255),
    "sorted":   (210, 255, 220),
    "pivot":    (255, 245, 200),
}

FOOTER_H = 48   # footer section এর height


class SortingVisualizer:
    def __init__(self, state):
        self.state      = state
        self.font_title = pygame.font.SysFont("Consolas", 13, bold=True)

    def draw(self, surface):
        hh = 36   # header height

        # ── Background ────────────────────────────────────────────────────────
        pygame.draw.rect(surface, C_BG,
                         pygame.Rect(VIZ_X, CANVAS_TOP, VIZ_W, CANVAS_H))

        # ── Header bar ────────────────────────────────────────────────────────
        pygame.draw.rect(surface, (12, 18, 32),
                         pygame.Rect(VIZ_X, CANVAS_TOP, VIZ_W, hh))
        pygame.draw.line(surface, C_BORDER,
                         (VIZ_X, CANVAS_TOP + hh), (VIZ_X + VIZ_W, CANVAS_TOP + hh))
        pygame.draw.circle(surface, (57, 255, 20),
                           (VIZ_X + 14, CANVAS_TOP + hh // 2), 5)
        lbl = self.font_title.render("VISUALIZATION", True, (136, 153, 187))
        surface.blit(lbl, (VIZ_X + 28, CANVAS_TOP + hh // 2 - lbl.get_height() // 2))

        # Search algo — target label in header
        if self.state.is_search_algo and self.state.search_target is not None:
            f_info = pygame.font.SysFont("Consolas", 12, bold=True)
            tgt = f_info.render(f"Target = {self.state.search_target}", True, (255, 214, 10))
            surface.blit(tgt, (VIZ_X + VIZ_W - tgt.get_width() - 16,
                               CANVAS_TOP + hh // 2 - tgt.get_height() // 2))

        arr = self.state.array
        if not arr:
            return

        n  = len(arr)
        mx = max(arr)

        margin     = BAR_AREA_MARGIN
        usable_w   = VIZ_W - 2 * margin
        bar_w      = max(2, (usable_w - (n - 1) * BAR_PADDING) // n)

        # Bar area — footer এর জন্য নিচে FOOTER_H + legend এর জায়গা রাখছি
        legend_h   = 28
        bar_area_h = CANVAS_H - hh - 8 - FOOTER_H - legend_h - 8

        # ── Bars ──────────────────────────────────────────────────────────────
        for i, val in enumerate(arr):
            x      = VIZ_X + margin + i * (bar_w + BAR_PADDING)
            bar_h  = max(4, int(val / mx * bar_area_h))
            y      = CANVAS_TOP + hh + 8 + (bar_area_h - bar_h)
            state  = self.state.bar_states.get(i, "default")
            colour = COLOUR_MAP.get(state, C_BAR_DEFAULT)

            pygame.draw.rect(surface, colour,
                             pygame.Rect(x, y, bar_w, bar_h), border_radius=2)

        # Baseline under bars
        by = CANVAS_TOP + hh + 8 + bar_area_h
        pygame.draw.line(surface, (30, 45, 70),
                         (VIZ_X + margin, by), (VIZ_X + VIZ_W - margin, by), 1)

        # ── Footer: number boxes ──────────────────────────────────────────────
        footer_y = CANVAS_TOP + CANVAS_H - legend_h - FOOTER_H - 4
        self._draw_footer(surface, arr, n, footer_y)

        # ── Legend ────────────────────────────────────────────────────────────
        self._legend(surface, CANVAS_TOP + CANVAS_H - legend_h)

    # ─────────────────────────────────────────────────────────────────────────
    def _draw_footer(self, surface, arr, n, footer_y):
        """
        Array values গুলো footer এ colored boxes এ দেখায়।
        Blue = idle, Red = active/comparing/swap, Green = sorted
        """
        margin   = BAR_AREA_MARGIN
        usable_w = VIZ_W - 2 * margin
        gap      = 2 if n > 30 else 3
        box_w    = max(10, min(44, (usable_w - (n - 1) * gap) // n))
        box_h = FOOTER_H - 8

        # font size
        if box_w >= 36: fs = 12
        elif box_w >= 26: fs = 11
        elif box_w >= 18: fs = 9
        else: fs = 8
        val_font = pygame.font.SysFont("Consolas", fs, bold=True)

        # Footer background strip
        pygame.draw.rect(surface, (10, 16, 28),
                         pygame.Rect(VIZ_X, footer_y, VIZ_W, FOOTER_H),
                         border_radius=4)
        pygame.draw.line(surface, (30, 45, 70),
                         (VIZ_X + margin, footer_y),
                         (VIZ_X + VIZ_W - margin, footer_y), 1)

        # Total width of all boxes
        total_w = n * box_w + (n - 1) * gap
        # Center horizontally
        start_x = VIZ_X + margin + (usable_w - total_w) // 2
        box_y   = footer_y + (FOOTER_H - box_h) // 2

        for i, val in enumerate(arr):
            bx    = start_x + i * (box_w + gap)
            st    = self.state.bar_states.get(i, "default")
            bg    = FOOTER_BOX_BG.get(st, FOOTER_BOX_BG["default"])
            bord  = FOOTER_BOX_BORDER.get(st, FOOTER_BOX_BORDER["default"])
            tc    = FOOTER_TEXT.get(st, FOOTER_TEXT["default"])

            # Search algo — eliminated boxes আরও dim
            if self.state.is_search_algo and st == "default":
                bg   = (12, 20, 38)
                bord = (25, 36, 58)
                tc   = (40, 55, 90)

            # Box
            pygame.draw.rect(surface, bg,
                             pygame.Rect(bx, box_y, box_w, box_h), border_radius=4)
            pygame.draw.rect(surface, bord,
                             pygame.Rect(bx, box_y, box_w, box_h), 1, border_radius=4)

            # Value text — centered
            v_surf = val_font.render(str(val), True, tc)
            vx = bx + (box_w - v_surf.get_width()) // 2
            vy = box_y + (box_h - v_surf.get_height()) // 2
            surface.blit(v_surf, (vx, vy))

    # ─────────────────────────────────────────────────────────────────────────
    def _legend(self, surface, y):
        font = pygame.font.SysFont("Consolas", 10)
        algo = self.state.algo_name
        if algo in ("Binary Search", "Linear Search"):
            items = [("Checking", FOOTER_BOX_BG["active"]),
                     ("Visited",  FOOTER_BOX_BG["compared"]),
                     ("Found",    FOOTER_BOX_BG["sorted"])]
        elif algo == "Quick Sort":
            items = [("Comparing", FOOTER_BOX_BG["active"]),
                     ("Pivot",     FOOTER_BOX_BG["pivot"]),
                     ("Swapping",  FOOTER_BOX_BG["swap"]),
                     ("Placed",    FOOTER_BOX_BG["sorted"])]
        elif algo == "Insertion Sort":
            items = [("Key",      FOOTER_BOX_BG["active"]),
                     ("Shifting", FOOTER_BOX_BG["swap"]),
                     ("Inserted", FOOTER_BOX_BG["pivot"]),
                     ("Sorted",   FOOTER_BOX_BG["sorted"])]
        else:
            items = [("Comparing", FOOTER_BOX_BG["active"]),
                     ("Secondary", FOOTER_BOX_BG["compared"]),
                     ("Swapping",  FOOTER_BOX_BG["swap"]),
                     ("Sorted",    FOOTER_BOX_BG["sorted"])]

        x = VIZ_X + BAR_AREA_MARGIN
        for label, col in items:
            pygame.draw.rect(surface, col,
                             pygame.Rect(x, y + 4, 10, 10), border_radius=2)
            t = font.render(label, True, C_TEXT_DIM)
            surface.blit(t, (x + 14, y + 2))
            x += t.get_width() + 30

    # ─────────────────────────────────────────────────────────────────────────
    def reset_states(self):
        self.state.bar_states = {i: "default" for i in range(len(self.state.array))}

    def apply_step(self, step, code_pnl, expl_pnl):
        s = self.state
        s.bar_states = {i: "default" for i in range(len(step["arr"]))}
        for idx, ck in step["highlights"].items():
            s.bar_states[idx] = ck
        s.array = step["arr"]
        stat = step.get("stat")
        if stat == "compare": s.comparisons += 1
        elif stat == "swap":  s.swaps += 1
        s.status_msg = step.get("info", "")
        code_pnl.set_line_from_stat(stat)
        expl_pnl.push_step(step.get("info", ""))
