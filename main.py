# =============================================================================
# main.py  —  AlgoViz Desktop
# ============================
# এটি প্রধান file। এখান থেকেই program শুরু হয়।
#
# দুটো Screen (Scene) আছে:
#   1. HomeScreen    — শুরুতে দেখায় (splash screen)
#   2. VisualizerScene — 3-panel visualizer
#                        [ CODE | VISUALIZATION | EXPLANATION ]
#
# VS Code এ চালানোর নিয়ম:
#   1. Terminal খোলো (Ctrl + `)
#   2. লেখো:  pip install pygame
#   3. লেখো:  python main.py
#
# Keyboard shortcuts:
#   ENTER / SPACE  →  Start (home এ) | Start / Pause (visualizer এ)
#   H              →  Home screen এ ফিরে যাও
#   R              →  Reset
#   N              →  নতুন random array
#   - / =          →  Speed কমাও / বাড়াও
#   ESC            →  বন্ধ করো
# =============================================================================

import sys
import random
import pygame

# আমাদের নিজেদের module গুলো import করছি
from core.constants import (
    WIDTH, HEIGHT, FPS, TITLE,
    C_BORDER, CODE_W, VIZ_X, VIZ_W,
    CANVAS_TOP, CANVAS_H,
)
from core.state              import AppState
from ui.home_screen          import HomeScreen
from ui.control_panel        import ControlPanel
from ui.status_bar           import StatusBar
from ui.code_panel           import CodePanel
from ui.explanation_panel    import ExplanationPanel
from visualizer.sorting_view     import SortingVisualizer
from visualizer.pathfinding_view import PathfindingVisualizer
from algorithms import SORTING_REGISTRY, PATH_REGISTRY


# =============================================================================
# VisualizerScene — 3-panel algorithm visualizer
# =============================================================================
class VisualizerScene:
    """
    মূল visualizer screen।
    তিনটি panel:
      - বাম  (CodePanel)       : Python code, active line highlight
      - মাঝে (Sorting/Pathfinding Visualizer): animation
      - ডান  (ExplanationPanel): step description, complexity, stats
    """

    def __init__(self, state):
        self.state     = state

        # সব UI component তৈরি করছি
        self.ctrl      = ControlPanel(state)        # উপরের control bar
        self.status    = StatusBar(state)           # নিচের status bar
        self.code_pnl  = CodePanel(state)           # বাম panel
        self.expl_pnl  = ExplanationPanel(state)    # ডান panel
        self.sort_view = SortingVisualizer(state)   # মাঝের sorting view
        self.path_view = PathfindingVisualizer(state) # মাঝের pathfinding view

        # শুরুতে একটা random array এবং grid তৈরি করছি
        self._gen_array()
        self.path_view.init_grid()

    # -------------------------------------------------------------------------
    # Public API — ControlPanel এবং keyboard থেকে এই methods call হয়
    # -------------------------------------------------------------------------

    def start(self):
        """Algorithm animation শুরু করো।"""
        if self.state.running and not self.state.finished:
            return  # আগেই চলছে

        # State reset করছি
        self.state.reset_stats()
        self.state.finished   = False
        self.state.paused     = False
        self.state.step_timer = 0
        self.expl_pnl.reset()
        self.code_pnl.active_line = -1

        if self.state.mode == "sorting":
            fn = SORTING_REGISTRY[self.state.algo_name]
            # Search algorithms এর জন্য target value পাঠাই
            if self.state.is_search_algo:
                self.state.generator = fn(list(self.state.array),
                                          self.state.search_target)
            else:
                self.state.generator = fn(list(self.state.array))
            self.sort_view.reset_states()
        else:
            # Pathfinding algorithm এর generator তৈরি করছি
            self.path_view.reset_paths()
            fn   = PATH_REGISTRY[self.state.algo_name]
            grid = [row[:] for row in self.state.grid]  # grid এর copy নিচ্ছি
            self.state.generator = fn(
                grid, self.state.start_cell, self.state.end_cell
            )

        self.state.running    = True
        self.state.status_msg = f"Running {self.state.algo_name}..."

    def toggle_pause(self):
        """Pause / Resume করো।"""
        if not self.state.running or self.state.finished:
            return
        self.state.paused = not self.state.paused
        self.state.status_msg = (
            "Paused — press Resume to continue"
            if self.state.paused
            else f"Resumed {self.state.algo_name}..."
        )

    def reset(self):
        """সব কিছু reset করো।"""
        self.state.stop()
        self.state.reset_stats()
        self.expl_pnl.reset()
        self.code_pnl.active_line = -1
        self.state.status_msg = "Ready — select an algorithm and press Start"

        if self.state.mode == "sorting":
            self._gen_array()
            self.sort_view.reset_states()
        else:
            self.path_view.reset_paths()

    def reset_grid(self):
        """Grid সম্পূর্ণ পরিষ্কার করো।"""
        self.state.stop()
        self.state.reset_stats()
        self.expl_pnl.reset()
        self.path_view.init_grid()
        self.state.status_msg = "Grid cleared"

    def randomise_array(self):
        """নতুন random array তৈরি করো।"""
        self.reset()
        self._gen_array()

    # -------------------------------------------------------------------------
    # Internal helpers
    # -------------------------------------------------------------------------

    def _gen_array(self):
        """Random array generate করে।"""
        n = self.state.bar_count
        self.state.array = random.sample(range(4, 100), min(n, 96))
        self.sort_view.reset_states()

    def _advance(self):
        """
        Generator থেকে পরবর্তী step নিয়ে visualizer এ apply করে।
        প্রতি frame এ এটি call হয়।
        """
        s = self.state
        if not s.running or s.paused or s.finished or s.generator is None:
            return  # চলার দরকার নেই

        # Slow speed এ কিছু frame অপেক্ষা করতে হয়
        if s.delay_frames > 0:
            s.step_timer += 1
            if s.step_timer < s.delay_frames:
                return
            s.step_timer = 0

        # Speed অনুযায়ী এক frame এ কতটি step নেব
        for _ in range(s.steps_per_frame):
            try:
                step = next(s.generator)  # generator থেকে পরের step
            except StopIteration:
                # Generator শেষ হয়ে গেছে
                s.finished    = True
                s.running     = False
                s.status_msg  = f"Done! {s.algo_name} complete."
                self.expl_pnl.push_step("Algorithm finished!")
                return

            # Step টি সঠিক visualizer এ পাঠাচ্ছি
            if s.mode == "sorting":
                self.sort_view.apply_step(step, self.code_pnl, self.expl_pnl)
            else:
                self.path_view.apply_step(step, self.code_pnl, self.expl_pnl)

            self.expl_pnl.total_steps = self.expl_pnl.cur_step

            if step.get("done"):
                s.finished = True
                s.running  = False
                return

    # -------------------------------------------------------------------------
    # Per-frame: handle event, update, draw
    # -------------------------------------------------------------------------

    def handle_event(self, event):
        """
        Event handle করো।
        'home' return করলে home screen এ যাবে।
        """
        if event.type == pygame.KEYDOWN:
            k = event.key
            if k == pygame.K_h:
                # H চাপলে home এ ফিরে যাই
                self.state.stop()
                return "home"
            elif k in (pygame.K_SPACE, pygame.K_RETURN):
                if not self.state.running or self.state.finished:
                    self.start()
                else:
                    self.toggle_pause()
            elif k == pygame.K_r:      self.reset()
            elif k == pygame.K_n:      self.randomise_array()
            elif k == pygame.K_ESCAPE: pygame.quit(); sys.exit()
            elif k == pygame.K_MINUS:
                self.state.speed = max(1, self.state.speed - 1)
                self.ctrl.slider.value = self.state.speed
            elif k == pygame.K_EQUALS:
                self.state.speed = min(10, self.state.speed + 1)
                self.ctrl.slider.value = self.state.speed

        # Control panel এ event পাঠাচ্ছি
        self.ctrl.handle_event(event, self)

        # Pathfinding mode এ grid এ mouse click handle করছি
        if self.state.mode == "pathfinding":
            placing = self.ctrl.placing_mode
            self.path_view.handle_event(event, placing)
            # Cell place করার পরে placing mode বন্ধ করছি
            if placing in ("start", "end") and event.type == pygame.MOUSEBUTTONDOWN:
                cell = self.path_view._cell_at(*event.pos)
                if cell is not None:
                    self.ctrl.placing_mode = None
                    self.state.status_msg  = "Ready"

        return None

    def update(self, mouse_pos):
        """প্রতি frame এ state update করো।"""
        self.ctrl.update(mouse_pos)
        self._advance()

    def draw(self, surface):
        """সব কিছু আঁকো।"""
        surface.fill((10, 14, 22))

        # তিনটি panel আঁকছি
        self.code_pnl.draw(surface)   # বাম: code

        if self.state.mode == "sorting":
            self.sort_view.draw(surface)    # মাঝে: bars
        else:
            self.path_view.draw(surface)    # মাঝে: grid

        self.expl_pnl.draw(surface)   # ডান: explanation

        # তিনটি panel এর মাঝে divider line
        pygame.draw.line(surface, C_BORDER,
                         (CODE_W, CANVAS_TOP),
                         (CODE_W, CANVAS_TOP + CANVAS_H), 1)
        pygame.draw.line(surface, C_BORDER,
                         (VIZ_X + VIZ_W, CANVAS_TOP),
                         (VIZ_X + VIZ_W, CANVAS_TOP + CANVAS_H), 1)

        # উপর ও নিচের bar
        self.ctrl.draw(surface)
        self.status.draw(surface)

        # "H = Home" hint
        f = pygame.font.SysFont("Consolas", 11)
        hint = f.render("H = Home", True, (45, 60, 85))
        surface.blit(hint, (WIDTH - hint.get_width() - 14, HEIGHT - 50))


# =============================================================================
# App — Scene Manager (Home ↔ Visualizer)
# =============================================================================
class App:
    """
    প্রধান Application class।
    দুটো scene manage করে:
      - "home"       : HomeScreen
      - "visualizer" : VisualizerScene
    """

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)

        # Window তৈরি করছি — screen এর সাথে মিলিয়ে size করা হয়েছে
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock  = pygame.time.Clock()

        # Shared state — দুই scene এই একই state share করে
        self.state = AppState()

        # দুটো scene তৈরি করছি
        self.home_scene = HomeScreen()
        self.viz_scene  = VisualizerScene(self.state)

        # শুরুতে home screen দেখাবে
        self.scene = "home"

    def run(self):
        """Main game loop — প্রতি frame এ চলে।"""
        while True:
            self.clock.tick(FPS)  # FPS নিয়ন্ত্রণ করছি
            mouse = pygame.mouse.get_pos()
            self.state.fps_display = int(self.clock.get_fps())

            # --- Events handle করছি -------------------------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.scene == "home":
                    # Home screen এর event
                    result = self.home_scene.handle_event(event)
                    if result == "visualizer":
                        self.scene = "visualizer"
                        self.state.status_msg = "Ready — select algorithm and press Start"
                    elif result == "quit":
                        pygame.quit()
                        sys.exit()

                elif self.scene == "visualizer":
                    # Visualizer এর event
                    result = self.viz_scene.handle_event(event)
                    if result == "home":
                        self.scene = "home"

            # --- Update -----------------------------------------------------------
            if self.scene == "home":
                self.home_scene.update(mouse)
            elif self.scene == "visualizer":
                self.viz_scene.update(mouse)

            # --- Draw -------------------------------------------------------------
            if self.scene == "home":
                self.home_scene.draw(self.screen)
            elif self.scene == "visualizer":
                self.viz_scene.draw(self.screen)

            pygame.display.flip()  # Screen update করছি


# =============================================================================
# Entry point — python main.py দিলে এখান থেকে শুরু হয়
# =============================================================================
if __name__ == "__main__":
    App().run()
