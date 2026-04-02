"""
Home Screen — shown when the app launches.
Animated background, title, feature cards, algorithm list, Start button.
Press Start or ENTER to go to the visualizer.
"""
import pygame
import math
import random
from core.constants import (
    WIDTH, HEIGHT,
    C_BG, C_PANEL, C_BORDER, C_BORDER_BRIGHT,
    C_CYAN, C_GREEN, C_ORANGE, C_PURPLE, C_YELLOW, C_RED, C_PINK,
    C_TEXT, C_TEXT_DIM, C_TEXT_MUTED,
    C_BTN_NORMAL, C_BTN_HOVER,
)


class Particle:
    """Floating background particle."""
    def __init__(self):
        self.reset()

    def reset(self):
        self.x   = random.randint(0, WIDTH)
        self.y   = random.randint(0, HEIGHT)
        self.vx  = random.uniform(-0.3, 0.3)
        self.vy  = random.uniform(-0.5, -0.1)
        self.r   = random.randint(1, 3)
        self.col = random.choice([C_CYAN, C_GREEN, C_PURPLE, C_ORANGE])
        self.alpha = random.randint(40, 140)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.alpha -= 0.4
        if self.y < -10 or self.alpha <= 0:
            self.reset()
            self.y = HEIGHT + 5


class AnimBar:
    """A single demo bar that animates on the home screen."""
    def __init__(self, x, target_h, colour, delay):
        self.x        = x
        self.target_h = target_h
        self.cur_h    = 0
        self.colour   = colour
        self.delay    = delay   # frames before starting rise
        self.frame    = 0
        self.w        = 18

    def update(self):
        self.frame += 1
        if self.frame > self.delay:
            diff = self.target_h - self.cur_h
            self.cur_h += diff * 0.12
            if abs(diff) < 0.5:
                self.cur_h = self.target_h

    def draw(self, surface, base_y):
        if self.cur_h < 2:
            return
        h = int(self.cur_h)
        rect = pygame.Rect(self.x, base_y - h, self.w, h)
        pygame.draw.rect(surface, self.colour, rect, border_radius=3)
        glow = pygame.Surface((self.w, h), pygame.SRCALPHA)
        glow.fill((*self.colour, 35))
        surface.blit(glow, (self.x, base_y - h))


class HomeScreen:
    """Full home/splash screen drawn before the visualizer."""

    def __init__(self):
        pygame.font.init()

        # Fonts
        self.f_giant  = pygame.font.SysFont("Arial",    72, bold=True)
        self.f_title  = pygame.font.SysFont("Arial",    28, bold=True)
        self.f_sub    = pygame.font.SysFont("Consolas", 15)
        self.f_md     = pygame.font.SysFont("Consolas", 13, bold=True)
        self.f_sm     = pygame.font.SysFont("Consolas", 12)
        self.f_card   = pygame.font.SysFont("Arial",    13, bold=True)
        self.f_tag    = pygame.font.SysFont("Consolas", 11)

        # Particles
        self.particles = [Particle() for _ in range(60)]

        # Demo animated bars (bottom-left area)
        bar_data = [
            (30,  80,  C_BAR_COLOURS[0], 10),
            (52,  140, C_BAR_COLOURS[1], 18),
            (74,  60,  C_BAR_COLOURS[2], 26),
            (96,  180, C_BAR_COLOURS[3], 12),
            (118, 110, C_BAR_COLOURS[4], 20),
            (140, 50,  C_BAR_COLOURS[5], 8),
            (162, 160, C_BAR_COLOURS[6], 24),
            (184, 90,  C_BAR_COLOURS[7], 16),
        ]
        self.bars = [AnimBar(x, h, c, d) for x, h, c, d in bar_data]
        self.bar_base_y = HEIGHT - 80

        # Button
        self.btn_rect    = pygame.Rect(WIDTH//2 - 130, HEIGHT - 170, 260, 56)
        self.btn_hovered = False
        self.btn_about_rect = pygame.Rect(WIDTH//2 - 65, HEIGHT - 100, 130, 36)
        self.btn_about_hovered = False

        # Animation tick
        self.tick    = 0
        self.alpha_in = 0   # fade-in counter

    def handle_event(self, event):
        """Return 'visualizer', 'quit', or None."""
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                return "visualizer"
            if event.key == pygame.K_ESCAPE:
                return "quit"

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.btn_rect.collidepoint(event.pos):
                return "visualizer"
            if self.btn_about_rect.collidepoint(event.pos):
                return None   # could open about — stay for now

        return None

    def update(self, mouse_pos):
        self.tick += 1
        self.alpha_in = min(255, self.alpha_in + 4)
        self.btn_hovered       = self.btn_rect.collidepoint(mouse_pos)
        self.btn_about_hovered = self.btn_about_rect.collidepoint(mouse_pos)
        for p in self.particles:
            p.update()
        for b in self.bars:
            b.update()

    def draw(self, surface):
        surface.fill(C_BG)
        self._draw_grid(surface)
        self._draw_particles(surface)
        self._draw_bars(surface)
        self._draw_glow(surface)
        self._draw_content(surface)
        self._draw_buttons(surface)
        self._draw_footer(surface)

    # ── Background grid ───────────────────────────────────────────────────────
    def _draw_grid(self, surface):
        gs = 48
        for x in range(0, WIDTH, gs):
            pygame.draw.line(surface, (18, 27, 44), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, gs):
            pygame.draw.line(surface, (18, 27, 44), (0, y), (WIDTH, y))

    # ── Particles ─────────────────────────────────────────────────────────────
    def _draw_particles(self, surface):
        for p in self.particles:
            s = pygame.Surface((p.r*2, p.r*2), pygame.SRCALPHA)
            pygame.draw.circle(s, (*p.col, int(p.alpha)), (p.r, p.r), p.r)
            surface.blit(s, (int(p.x)-p.r, int(p.y)-p.r))

    # ── Animated demo bars (bottom-left) ─────────────────────────────────────
    def _draw_bars(self, surface):
        bx = 30
        for b in self.bars:
            b.draw(surface, self.bar_base_y)
        # Baseline
        pygame.draw.line(surface, C_BORDER,
                         (bx - 4, self.bar_base_y),
                         (bx + len(self.bars)*22 + 10, self.bar_base_y), 1)

    # ── Central radial glow ───────────────────────────────────────────────────
    def _draw_glow(self, surface):
        pulse = 0.5 + 0.5 * math.sin(self.tick * 0.03)
        r = int(320 + pulse * 30)
        glow = pygame.Surface((r*2, r*2), pygame.SRCALPHA)
        for i in range(5):
            alpha = int((5-i) * 6)
            pygame.draw.circle(glow, (0, 229, 255, alpha),
                               (r, r), r - i*40)
        surface.blit(glow, (WIDTH//2 - r, HEIGHT//2 - r - 60))

    # ── Main text content ─────────────────────────────────────────────────────
    def _draw_content(self, surface):
        cx = WIDTH // 2
        alpha = min(255, self.alpha_in)

        # ── Badge ─────────────────────────────────────────────────────────────
        badge_y = 68
        badge_txt = self.f_tag.render("✦  INTERACTIVE LEARNING PLATFORM  ✦", True, C_CYAN)
        bw = badge_txt.get_width() + 32
        bh = 28
        bx = cx - bw//2
        pygame.draw.rect(surface, (0, 40, 55),
                         pygame.Rect(bx, badge_y, bw, bh), border_radius=14)
        pygame.draw.rect(surface, (0, 80, 100),
                         pygame.Rect(bx, badge_y, bw, bh), 1, border_radius=14)
        surface.blit(badge_txt, (cx - badge_txt.get_width()//2, badge_y + 6))

        # ── Giant Title ───────────────────────────────────────────────────────
        title1 = self.f_giant.render("AlgoViz", True, C_TEXT)
        title2 = self.f_giant.render("Desktop", True, C_CYAN)
        ty = 108
        surface.blit(title1, (cx - (title1.get_width() + title2.get_width() + 16)//2, ty))
        surface.blit(title2, (cx - (title1.get_width() + title2.get_width() + 16)//2 + title1.get_width() + 16, ty))

        # ── Subtitle ──────────────────────────────────────────────────────────
        sub = self.f_sub.render("See algorithms come alive — step by step, in real time.", True, C_TEXT_DIM)
        surface.blit(sub, (cx - sub.get_width()//2, ty + 82))

        # ── Feature cards row ─────────────────────────────────────────────────
        cards = [
            ("⚡", "Real-Time",    "Every swap &\ncomparison animated",   C_CYAN),
            ("📄", "Live Code",    "Python source\nhighlights each step",  C_GREEN),
            ("📖", "Explanation",  "Plain-English\nstep descriptions",     C_ORANGE),
            ("🎛️", "Controls",     "Start, Pause,\nReset + Speed slider",  C_PURPLE),
        ]
        card_w, card_h = 210, 100
        gap = 20
        total_w = len(cards) * card_w + (len(cards)-1) * gap
        start_x = cx - total_w // 2
        card_y  = 230

        for i, (icon, title, desc, col) in enumerate(cards):
            x = start_x + i * (card_w + gap)
            cr = pygame.Rect(x, card_y, card_w, card_h)
            pygame.draw.rect(surface, (16, 24, 40), cr, border_radius=12)
            pygame.draw.rect(surface, C_BORDER, cr, 1, border_radius=12)
            # Top accent line
            pygame.draw.rect(surface, col,
                             pygame.Rect(x+1, card_y+1, card_w-2, 3), border_radius=12)
            # Icon
            ic = self.f_title.render(icon, True, col)
            surface.blit(ic, (x+16, card_y+14))
            # Title
            tl = self.f_card.render(title, True, C_TEXT)
            surface.blit(tl, (x+16, card_y+46))
            # Desc
            for di, dline in enumerate(desc.split("\n")):
                dl = self.f_tag.render(dline, True, C_TEXT_DIM)
                surface.blit(dl, (x+16, card_y+64 + di*14))

        # ── Algorithm pills ───────────────────────────────────────────────────
        algo_y = 354
        pill_label = self.f_sm.render("Available Algorithms:", True, C_TEXT_MUTED)
        surface.blit(pill_label, (cx - pill_label.get_width()//2, algo_y))
        algo_y += 24

        pills = [
            ("Bubble Sort",    C_CYAN,   "sorting"),
            ("Selection Sort", C_GREEN,  "sorting"),
            ("Merge Sort",     C_PURPLE, "sorting"),
            ("BFS",            C_ORANGE, "path"),
            ("Dijkstra",       C_YELLOW, "path"),
        ]
        pill_total = sum(self.f_md.size(p[0])[0] + 40 for p in pills) + (len(pills)-1)*10
        px = cx - pill_total // 2

        for name, col, kind in pills:
            tw = self.f_md.size(name)[0]
            pw = tw + 40
            pr = pygame.Rect(px, algo_y, pw, 30)
            pygame.draw.rect(surface, (*col, 25), pr, border_radius=15)
            pygame.draw.rect(surface, (*col, 80), pr, 1, border_radius=15)
            nt = self.f_md.render(name, True, col)
            surface.blit(nt, (px + 20, algo_y + 7))
            px += pw + 10

        # ── "3-Panel Layout" diagram preview ──────────────────────────────────
        diag_y = 420
        diag_w, diag_h = 560, 68
        diag_x = cx - diag_w // 2
        pygame.draw.rect(surface, (14, 20, 36),
                         pygame.Rect(diag_x, diag_y, diag_w, diag_h), border_radius=10)
        pygame.draw.rect(surface, C_BORDER,
                         pygame.Rect(diag_x, diag_y, diag_w, diag_h), 1, border_radius=10)

        sections = [
            ("◉ CODE",          C_CYAN,   diag_x + 6,            140),
            ("◉ VISUALIZATION", C_GREEN,  diag_x + 6 + 148,      270),
            ("◉ EXPLANATION",   C_ORANGE, diag_x + 6 + 148 + 278, 134),
        ]
        for label, col, sx, sw in sections:
            sr = pygame.Rect(sx, diag_y + 6, sw, diag_h - 12)
            pygame.draw.rect(surface, (20, 30, 50), sr, border_radius=7)
            pygame.draw.rect(surface, (*col, 60), sr, 1, border_radius=7)
            lt = self.f_tag.render(label, True, col)
            surface.blit(lt, (sx + sw//2 - lt.get_width()//2, diag_y + 26))

        arrow_t = self.f_sm.render("The 3-panel layout — just like the web version", True, C_TEXT_MUTED)
        surface.blit(arrow_t, (cx - arrow_t.get_width()//2, diag_y + diag_h + 8))

        # ── Team credit ───────────────────────────────────────────────────────
        team = self.f_tag.render(
            "Shajada Masum  ·  Sabur  ·  Sojib  ·  Joy  ·  Saikot",
            True, C_TEXT_MUTED)
        surface.blit(team, (cx - team.get_width()//2, diag_y + diag_h + 32))

    # ── Buttons ───────────────────────────────────────────────────────────────
    def _draw_buttons(self, surface):
        # Main START button
        col = C_CYAN if self.btn_hovered else (0, 180, 210)
        pygame.draw.rect(surface, col, self.btn_rect, border_radius=12)
        if self.btn_hovered:
            glow = pygame.Surface((self.btn_rect.w+20, self.btn_rect.h+20), pygame.SRCALPHA)
            pygame.draw.rect(glow, (0, 229, 255, 40),
                             pygame.Rect(10,10,self.btn_rect.w,self.btn_rect.h), border_radius=12)
            surface.blit(glow, (self.btn_rect.x-10, self.btn_rect.y-10))

        lbl = self.f_title.render("▶  Start Visualizing", True, (8, 12, 20))
        surface.blit(lbl, (self.btn_rect.centerx - lbl.get_width()//2,
                            self.btn_rect.centery - lbl.get_height()//2))

        # Hint
        hint = self.f_tag.render("Press  ENTER  or  SPACE  to start", True, C_TEXT_MUTED)
        surface.blit(hint, (WIDTH//2 - hint.get_width()//2,
                             self.btn_rect.bottom + 10))

    # ── Footer bar ────────────────────────────────────────────────────────────
    def _draw_footer(self, surface):
        fy = HEIGHT - 32
        pygame.draw.rect(surface, C_PANEL, pygame.Rect(0, fy, WIDTH, 32))
        pygame.draw.line(surface, C_BORDER, (0, fy), (WIDTH, fy), 1)

        left = self.f_tag.render("AlgoViz Desktop  —  Python + Pygame", True, C_TEXT_MUTED)
        right = self.f_tag.render("ESC to quit", True, C_TEXT_MUTED)
        surface.blit(left,  (16, fy + 8))
        surface.blit(right, (WIDTH - right.get_width() - 16, fy + 8))


# Colour palette for animated bars
C_BAR_COLOURS = [
    (0, 229, 255), (57, 255, 20), (191, 90, 242), (255, 107, 43),
    (255, 214, 10), (255, 69, 58), (30, 144, 255), (255, 45, 130),
]
