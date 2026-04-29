import pygame
from core.constants import (
    C_BTN_NORMAL, C_BTN_HOVER, C_BTN_DISABLED,
    C_BORDER, C_CYAN, C_TEXT, C_TEXT_MUTED, C_BORDER_BRIGHT,
)

class Button:
    def __init__(self, x, y, w, h, label, accent=False, toggle=False, font=None):
        self.rect    = pygame.Rect(x, y, w, h)
        self.label   = label
        self.accent  = accent
        self.toggle  = toggle
        self.pressed = False
        self.enabled = True
        self.hovered = False
        self._font   = font

    def set_font(self, f): self._font = f

    def handle_event(self, event):
        if not self.enabled: return False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.toggle: self.pressed = not self.pressed
                return True
        return False

    def update(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos) and self.enabled

    def draw(self, surface):
        if not self.enabled:      bg = C_BTN_DISABLED
        elif self.accent or (self.toggle and self.pressed): bg = C_CYAN
        elif self.hovered:        bg = C_BTN_HOVER
        else:                     bg = C_BTN_NORMAL
        pygame.draw.rect(surface, bg, self.rect, border_radius=8)
        pygame.draw.rect(surface, C_BORDER, self.rect, 1, border_radius=8)
        if self._font:
            col = (10,14,22) if (self.accent or (self.toggle and self.pressed)) else (
                C_TEXT_MUTED if not self.enabled else C_TEXT)
            t = self._font.render(self.label, True, col)
            surface.blit(t, t.get_rect(center=self.rect.center))


class Dropdown:
    def __init__(self, x, y, w, h, options, font=None):
        self.rect     = pygame.Rect(x, y, w, h)
        self.options  = options
        self.selected = 0
        self.open     = False
        self._font    = font
        self.hovered_item = -1

    def set_font(self, f): self._font = f

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.open = not self.open; return False
            if self.open:
                for i, r in enumerate(self._opt_rects()):
                    if r.collidepoint(event.pos):
                        changed = i != self.selected
                        self.selected = i; self.open = False; return changed
                self.open = False
        return False

    def update(self, mouse_pos):
        self.hovered_item = -1
        if self.open:
            for i, r in enumerate(self._opt_rects()):
                if r.collidepoint(mouse_pos): self.hovered_item = i

    def _opt_rects(self):
        return [pygame.Rect(self.rect.x, self.rect.bottom + i*self.rect.h,
                            self.rect.w, self.rect.h) for i in range(len(self.options))]

    def draw(self, surface):
        pygame.draw.rect(surface, C_BTN_NORMAL, self.rect, border_radius=6)
        pygame.draw.rect(surface, C_CYAN if self.open else C_BORDER, self.rect, 1, border_radius=6)
        if self._font:
            t = self._font.render(self.options[self.selected], True, C_TEXT)
            surface.blit(t, (self.rect.x+10, self.rect.y+(self.rect.h-t.get_height())//2))
            a = self._font.render("▾", True, C_TEXT_MUTED)
            surface.blit(a, (self.rect.right-20, self.rect.y+(self.rect.h-a.get_height())//2))
        if self.open:
            for i, r in enumerate(self._opt_rects()):
                bg = C_BTN_HOVER if i == self.hovered_item else C_BTN_NORMAL
                pygame.draw.rect(surface, bg, r)
                pygame.draw.rect(surface, C_BORDER, r, 1)
                if self._font:
                    col = C_CYAN if i == self.selected else C_TEXT
                    t = self._font.render(self.options[i], True, col)
                    surface.blit(t, (r.x+10, r.y+(r.h-t.get_height())//2))


class Slider:
    def __init__(self, x, y, w, h, mn, mx, val, label="Speed"):
        self.rect     = pygame.Rect(x, y, w, h)
        self.min_val  = mn; self.max_val = mx; self.value = val
        self.label    = label; self.dragging = False; self._font = None

    def set_font(self, f): self._font = f

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos): self.dragging = True; self._upd(event.pos[0])
        elif event.type == pygame.MOUSEBUTTONUP: self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging: self._upd(event.pos[0])

    def _upd(self, mx):
        r = max(0.0, min(1.0, (mx-self.rect.x)/self.rect.w))
        self.value = round(self.min_val + r*(self.max_val-self.min_val))

    def draw(self, surface):
        ty = self.rect.centery
        pygame.draw.rect(surface, C_BORDER_BRIGHT, (self.rect.x, ty-2, self.rect.w, 4), border_radius=2)
        r = (self.value-self.min_val)/(self.max_val-self.min_val)
        fw = int(self.rect.w*r)
        pygame.draw.rect(surface, C_CYAN, (self.rect.x, ty-2, fw, 4), border_radius=2)
        tx = self.rect.x + fw
        pygame.draw.circle(surface, C_CYAN, (tx, ty), 8)
        pygame.draw.circle(surface, (10,14,22), (tx, ty), 4)
        if self._font:
            l = self._font.render(f"{self.label}: {self.value}", True, C_TEXT_MUTED)
            surface.blit(l, (self.rect.x, self.rect.y-18))


class TextInput:
    """Comma-separated array input এবং single number input উভয়ের জন্য।"""
    def __init__(self, x, y, w, h, placeholder="e.g. 5,3,8,1,9", mode="array"):
        self.rect         = pygame.Rect(x, y, w, h)
        self.placeholder  = placeholder
        self.text         = ""
        self.active       = False
        self.cursor_vis   = True
        self.cursor_timer = 0
        self._font        = None
        self.error        = False
        self.mode         = mode  # "array" or "number"

    def set_font(self, f): self._font = f

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.error  = False
        if not self.active:
            return None
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]; self.error = False
            elif event.key == pygame.K_RETURN:
                return self._parse()
            elif event.key == pygame.K_ESCAPE:
                self.active = False
            else:
                allowed = "0123456789, " if self.mode == "array" else "0123456789"
                if event.unicode in allowed:
                    self.text += event.unicode; self.error = False
        return None

    def _parse(self):
        if self.mode == "number":
            try:
                v = int(self.text.strip())
                self.error = False; return v
            except ValueError:
                self.error = True; return None
        try:
            parts = [p.strip() for p in self.text.split(",") if p.strip()]
            if not parts: self.error = True; return None
            values = [int(p) for p in parts]
            if not (2 <= len(values) <= 50): self.error = True; return None
            if any(v < 1 or v > 200 for v in values): self.error = True; return None
            self.error = False; return values
        except ValueError:
            self.error = True; return None

    def update(self):
        self.cursor_timer += 1
        if self.cursor_timer >= 30:
            self.cursor_vis = not self.cursor_vis; self.cursor_timer = 0

    def draw(self, surface):
        from core.constants import C_BTN_NORMAL, C_BORDER, C_CYAN, C_TEXT, C_TEXT_MUTED
        pygame.draw.rect(surface, C_BTN_NORMAL, self.rect, border_radius=6)
        border_col = (255,69,58) if self.error else (C_CYAN if self.active else C_BORDER)
        pygame.draw.rect(surface, border_col, self.rect, 1, border_radius=6)
        if self._font:
            display = self.text if self.text else self.placeholder
            col = C_TEXT if self.text else C_TEXT_MUTED
            txt_surf = self._font.render(display, True, col)
            clip = pygame.Rect(self.rect.x+8, self.rect.y, self.rect.w-16, self.rect.h)
            surface.set_clip(clip)
            ty = self.rect.y + (self.rect.h - txt_surf.get_height()) // 2
            surface.blit(txt_surf, (self.rect.x+8, ty))
            surface.set_clip(None)
            if self.active and self.cursor_vis and self.text:
                cx = self.rect.x + 8 + min(txt_surf.get_width(), self.rect.w - 20) + 1
                pygame.draw.line(surface, C_CYAN,
                                 (cx, self.rect.y+6), (cx, self.rect.bottom-6), 2)
