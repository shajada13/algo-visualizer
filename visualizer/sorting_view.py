import pygame
from core.constants import (
    C_BG, C_BORDER, C_TEXT_MUTED, C_TEXT_DIM, C_TEXT,
    C_BAR_DEFAULT, C_BAR_ACTIVE, C_BAR_COMPARED,
    C_BAR_SWAP, C_BAR_SORTED, C_BAR_PIVOT,
    CANVAS_TOP, CANVAS_H, VIZ_X, VIZ_W,
    BAR_PADDING, BAR_AREA_MARGIN,
)

COLOUR_MAP = {
    "default":  C_BAR_DEFAULT,
    "active":   C_BAR_ACTIVE,
    "compared": C_BAR_COMPARED,
    "swap":     C_BAR_SWAP,
    "sorted":   C_BAR_SORTED,
    "pivot":    C_BAR_PIVOT,
}

# Active/highlighted bar এর value রঙ উজ্জ্বল হবে
VALUE_COLOUR_MAP = {
    "default":  (80, 100, 140),
    "active":   (0, 229, 255),      # cyan
    "compared": (255, 214, 10),     # yellow
    "swap":     (255, 100, 80),     # red-orange
    "sorted":   (57, 255, 20),      # green
    "pivot":    (191, 90, 242),     # purple
}


class SortingVisualizer:
    def __init__(self, state):
        self.state      = state
        self.font_title = pygame.font.SysFont("Consolas", 13, bold=True)

    def draw(self, surface):
        hh = 36
        pygame.draw.rect(surface, C_BG,
                         pygame.Rect(VIZ_X, CANVAS_TOP, VIZ_W, CANVAS_H))
        pygame.draw.rect(surface, (12, 18, 32),
                         pygame.Rect(VIZ_X, CANVAS_TOP, VIZ_W, hh))
        pygame.draw.line(surface, C_BORDER,
                         (VIZ_X, CANVAS_TOP + hh), (VIZ_X + VIZ_W, CANVAS_TOP + hh))
        pygame.draw.circle(surface, (57, 255, 20), (VIZ_X + 14, CANVAS_TOP + hh // 2), 5)
        lbl = self.font_title.render("VISUALIZATION", True, (136, 153, 187))
        surface.blit(lbl, (VIZ_X + 28, CANVAS_TOP + hh // 2 - lbl.get_height() // 2))

        arr = self.state.array
        if not arr:
            return

        n          = len(arr)
        mx         = max(arr)
        margin     = BAR_AREA_MARGIN
        usable_w   = VIZ_W - 2 * margin

        # bar width এবং font size — element সংখ্যা অনুযায়ী auto-adjust
        bar_w      = max(2, (usable_w - (n - 1) * BAR_PADDING) // n)
        font_size  = self._pick_font_size(n, bar_w)
        val_font   = pygame.font.SysFont("Consolas", font_size, bold=True) if font_size else None

        # value label এর জন্য নিচে জায়গা রাখছি
        label_h    = (font_size + 4) if font_size else 0
        bar_area_h = CANVAS_H - hh - 50 - label_h - 4

        for i, val in enumerate(arr):
            x      = VIZ_X + margin + i * (bar_w + BAR_PADDING)
            bar_h  = max(4, int(val / mx * bar_area_h))
            y      = CANVAS_TOP + hh + 8 + label_h + (bar_area_h - bar_h)
            state  = self.state.bar_states.get(i, "default")
            colour = COLOUR_MAP.get(state, C_BAR_DEFAULT)

            pygame.draw.rect(surface, colour,
                             pygame.Rect(x, y, bar_w, bar_h), border_radius=2)

            # ── Value label — bar এর নিচে ──────────────────────────────────
            if val_font:
                val_col = VALUE_COLOUR_MAP.get(state, (80, 100, 140))
                v_surf  = val_font.render(str(val), True, val_col)

                # label টা bar এর ঠিক নিচে baseline এ রাখছি
                lx = x + (bar_w - v_surf.get_width()) // 2
                ly = CANVAS_TOP + hh + 8 + label_h + bar_area_h + 4

                # active/swap হলে label টা bar এর উপরে তুলে দিচ্ছি — চোখে পড়বে
                if state in ("active", "compared", "swap"):
                    ly = y - v_surf.get_height() - 3
                    # ছোট background highlight
                    bg_r = pygame.Rect(lx - 2, ly - 1,
                                       v_surf.get_width() + 4, v_surf.get_height() + 2)
                    pygame.draw.rect(surface, (20, 28, 44), bg_r, border_radius=3)

                # clip করে surface boundary এর বাইরে না যায়
                surface.set_clip(pygame.Rect(VIZ_X, CANVAS_TOP, VIZ_W, CANVAS_H))
                surface.blit(v_surf, (lx, ly))
                surface.set_clip(None)
            # ───────────────────────────────────────────────────────────────

        # Baseline
        by = CANVAS_TOP + hh + 8 + label_h + bar_area_h + 2
        pygame.draw.line(surface, (30, 45, 70),
                         (VIZ_X + margin, by), (VIZ_X + VIZ_W - margin, by), 1)
        self._legend(surface, CANVAS_TOP + CANVAS_H - 24)

    def _pick_font_size(self, n, bar_w):
        """
        Element সংখ্যা ও bar width দেখে কত size font ব্যবহার করব।
        অনেক বেশি element হলে label বাদ দেব।
        """
        if n <= 15:   return 12
        if n <= 25:   return 11
        if n <= 35:   return 10
        if n <= 50 and bar_w >= 8:  return 9
        return 0   # অনেক বেশি — label দেখানো সম্ভব না

    def _legend(self, surface, y):
        font = pygame.font.SysFont("Consolas", 10)
        items = [("Comparing", C_BAR_ACTIVE), ("Secondary", C_BAR_COMPARED),
                 ("Swapping",  C_BAR_SWAP),   ("Sorted",    C_BAR_SORTED)]
        x = VIZ_X + BAR_AREA_MARGIN
        for label, col in items:
            pygame.draw.rect(surface, col, pygame.Rect(x, y + 4, 10, 10), border_radius=2)
            t = font.render(label, True, C_TEXT_DIM)
            surface.blit(t, (x + 14, y + 2))
            x += t.get_width() + 28

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
