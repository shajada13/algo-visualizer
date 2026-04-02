import pygame
from core.constants import (
    C_BG, C_BORDER, C_TEXT_DIM,
    C_CELL_DEFAULT, C_CELL_WALL, C_CELL_START, C_CELL_END,
    C_CELL_VISITED, C_CELL_FRONTIER, C_CELL_PATH,
    CANVAS_TOP, CANVAS_H, VIZ_X, VIZ_W,
    GRID_COLS, GRID_ROWS, CELL_SIZE,
)

CELL_COLOUR = {
    "empty":    C_CELL_DEFAULT,
    "wall":     C_CELL_WALL,
    "start":    C_CELL_START,
    "end":      C_CELL_END,
    "visited":  C_CELL_VISITED,
    "frontier": C_CELL_FRONTIER,
    "path":     C_CELL_PATH,
}


class PathfindingVisualizer:
    def __init__(self, state):
        self.state        = state
        self.font         = pygame.font.SysFont("Consolas", 11, bold=True)
        self.font_title   = pygame.font.SysFont("Consolas", 13, bold=True)
        self.font_leg     = pygame.font.SysFont("Consolas", 10)
        self._drawing_wall = False

    def init_grid(self):
        self.state.grid = [["empty"] * GRID_COLS for _ in range(GRID_ROWS)]
        self.state.start_cell = (GRID_ROWS // 2, 3)
        self.state.end_cell   = (GRID_ROWS // 2, GRID_COLS - 4)
        sr, sc = self.state.start_cell
        er, ec = self.state.end_cell
        self.state.grid[sr][sc] = "start"
        self.state.grid[er][ec] = "end"

    def reset_paths(self):
        g = self.state.grid
        if not g:
            return
        for r in range(GRID_ROWS):
            for c in range(GRID_COLS):
                if g[r][c] in ("visited", "frontier", "path"):
                    g[r][c] = "empty"
        self.state.nodes_visited = 0
        self.state.path_length   = 0

    def _cell_at(self, mx, my):
        hh = 36
        gx = mx - VIZ_X
        gy = my - CANVAS_TOP - hh
        if gx < 0 or gy < 0:
            return None
        col = gx // CELL_SIZE
        row = gy // CELL_SIZE
        if 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS:
            return (row, col)
        return None

    def handle_event(self, event, placing_mode):
        if self.state.running:
            return
        g = self.state.grid
        if not g:
            return
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            cell = self._cell_at(*event.pos)
            if cell is None:
                return
            r, c = cell
            if placing_mode == "start":
                sr, sc = self.state.start_cell
                if g[sr][sc] == "start": g[sr][sc] = "empty"
                self.state.start_cell = cell; g[r][c] = "start"
            elif placing_mode == "end":
                er, ec = self.state.end_cell
                if g[er][ec] == "end": g[er][ec] = "empty"
                self.state.end_cell = cell; g[r][c] = "end"
            else:
                if g[r][c] == "empty":
                    g[r][c] = "wall"; self._drawing_wall = True
                elif g[r][c] == "wall":
                    g[r][c] = "empty"; self._drawing_wall = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self._drawing_wall = False
        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0] and placing_mode is None:
                cell = self._cell_at(*event.pos)
                if cell:
                    r, c = cell
                    if g[r][c] not in ("start", "end"):
                        g[r][c] = "wall" if self._drawing_wall else "empty"

    def draw(self, surface):
        hh = 36
        pygame.draw.rect(surface, C_BG, pygame.Rect(VIZ_X, CANVAS_TOP, VIZ_W, CANVAS_H))
        pygame.draw.rect(surface, (12, 18, 32), pygame.Rect(VIZ_X, CANVAS_TOP, VIZ_W, hh))
        pygame.draw.line(surface, C_BORDER,
                         (VIZ_X, CANVAS_TOP + hh), (VIZ_X + VIZ_W, CANVAS_TOP + hh))
        pygame.draw.circle(surface, (57, 255, 20), (VIZ_X + 14, CANVAS_TOP + hh // 2), 5)
        lbl = self.font_title.render("VISUALIZATION", True, (136, 153, 187))
        surface.blit(lbl, (VIZ_X + 28, CANVAS_TOP + hh // 2 - lbl.get_height() // 2))

        g = self.state.grid
        if not g:
            return

        for r in range(GRID_ROWS):
            for c in range(GRID_COLS):
                cs = g[r][c]
                colour = CELL_COLOUR.get(cs, C_CELL_DEFAULT)
                x = VIZ_X + c * CELL_SIZE
                y = CANVAS_TOP + hh + r * CELL_SIZE
                pygame.draw.rect(surface, colour,
                                 pygame.Rect(x+1, y+1, CELL_SIZE-2, CELL_SIZE-2),
                                 border_radius=2)
                if cs in ("start", "end"):
                    ic = self.font.render("S" if cs == "start" else "E",
                                          True, (10, 14, 22))
                    surface.blit(ic, (x + (CELL_SIZE - ic.get_width()) // 2,
                                      y + (CELL_SIZE - ic.get_height()) // 2 + 1))

        # Legend
        leg_y = CANVAS_TOP + CANVAS_H - 22
        items = [("Start", C_CELL_START), ("End", C_CELL_END),
                 ("Visited", C_CELL_VISITED), ("Frontier", C_CELL_FRONTIER),
                 ("Path", C_CELL_PATH), ("Wall", C_CELL_WALL)]
        lx = VIZ_X + 12
        for label, col in items:
            pygame.draw.rect(surface, col, pygame.Rect(lx, leg_y+4, 10, 10), border_radius=2)
            t = self.font_leg.render(label, True, C_TEXT_DIM)
            surface.blit(t, (lx + 13, leg_y + 2))
            lx += t.get_width() + 22

    def apply_step(self, step, code_pnl, expl_pnl):
        g = self.state.grid
        if not g:
            return
        for (r, c), ns in step.get("grid_updates", {}).items():
            if g[r][c] not in ("start", "end"):
                g[r][c] = ns
        stat = step.get("stat")
        if stat == "visit": self.state.nodes_visited += 1
        elif stat == "path": self.state.path_length = len(step.get("path", []))
        self.state.status_msg = step.get("info", "")
        code_pnl.set_line_from_stat(stat)
        expl_pnl.push_step(step.get("info", ""))
