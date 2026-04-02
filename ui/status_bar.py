import pygame
from core.constants import (
    C_PANEL, C_BORDER, C_TEXT_DIM, C_TEXT_MUTED,
    C_CYAN, C_GREEN, C_ORANGE,
    WIDTH, HEIGHT, BOTTOM_PANEL_H,
)


class StatusBar:
    def __init__(self, state):
        self.state = state
        self.font  = pygame.font.SysFont("Consolas", 12)

    def draw(self, surface):
        y = HEIGHT - BOTTOM_PANEL_H
        pygame.draw.rect(surface, C_PANEL, (0, y, WIDTH, BOTTOM_PANEL_H))
        pygame.draw.line(surface, C_BORDER, (0, y), (WIDTH, y), 1)

        s = self.state
        if s.finished:   dot, status = C_GREEN,  "DONE"
        elif s.running and not s.paused: dot, status = C_CYAN, "RUNNING"
        elif s.paused:   dot, status = C_ORANGE, "PAUSED"
        else:            dot, status = C_TEXT_MUTED, "IDLE"

        pygame.draw.circle(surface, dot, (16, y + BOTTOM_PANEL_H // 2), 5)
        sl = self.font.render(f"[{status}]", True, dot)
        surface.blit(sl, (28, y + (BOTTOM_PANEL_H - sl.get_height()) // 2))

        msg = self.font.render((s.status_msg or "")[:110], True, C_TEXT_DIM)
        surface.blit(msg, (100, y + (BOTTOM_PANEL_H - msg.get_height()) // 2))

        fps = self.font.render(f"FPS: {s.fps_display}", True, C_TEXT_MUTED)
        surface.blit(fps, (WIDTH - fps.get_width() - 12,
                           y + (BOTTOM_PANEL_H - fps.get_height()) // 2))
