import pygame
from core.constants import (
    C_PANEL, C_BORDER, C_CYAN, C_TEXT, C_TEXT_DIM, C_TEXT_MUTED,
    C_GREEN, C_ORANGE, TOP_PANEL_H, WIDTH,
)
from ui.widgets import Button, Dropdown, Slider, TextInput


class ControlPanel:
    def __init__(self, state):
        self.state = state
        pygame.font.init()
        self.f_sm    = pygame.font.SysFont("Consolas", 12)
        self.f_md    = pygame.font.SysFont("Consolas", 13, bold=True)
        self.f_title = pygame.font.SysFont("Arial",    20, bold=True)
        self.f_sub   = pygame.font.SysFont("Consolas", 11)
        self.f_hint  = pygame.font.SysFont("Consolas", 10)

        self.tab_sort = Button(16,  14, 118, 34, "Sorting",     toggle=True)
        self.tab_path = Button(140, 14, 138, 34, "Pathfinding", toggle=True)
        self.tab_sort.pressed = True
        for b in (self.tab_sort, self.tab_path):
            b.set_font(self.f_md)

        self.dropdown = Dropdown(300, 14, 178, 34, state.algo_list)
        self.dropdown.set_font(self.f_md)

        self.btn_start  = Button(496, 14, 86, 34, "Start",  accent=True)
        self.btn_pause  = Button(588, 14, 86, 34, "Pause")
        self.btn_reset  = Button(680, 14, 86, 34, "Reset")
        self.btn_random = Button(496, 56, 80, 30, "Random")
        for b in (self.btn_start, self.btn_pause, self.btn_reset, self.btn_random):
            b.set_font(self.f_md)

        self.slider = Slider(790, 38, 148, 20, 1, 10, state.speed, "Speed")
        self.slider.set_font(self.f_sm)

        # Custom Array Input
        self.array_input = TextInput(582, 58, 190, 28,
                                     placeholder="e.g. 5,3,8,1,9", mode="array")
        self.array_input.set_font(self.f_sm)
        self.btn_apply   = Button(778, 58, 62, 28, "Apply")
        self.btn_apply.set_font(self.f_sm)

        # Search Target Input — Binary/Linear Search এর জন্য
        self.target_input = TextInput(582, 58, 120, 28,
                                      placeholder="target value", mode="number")
        self.target_input.set_font(self.f_sm)
        self.btn_set_target = Button(708, 58, 70, 28, "Set")
        self.btn_set_target.set_font(self.f_sm)

        self.input_msg       = ""
        self.input_msg_col   = C_CYAN
        self.input_msg_timer = 0

        # Pathfinding tools
        self.btn_set_start = Button(300, 56, 86, 30, "Set Start")
        self.btn_set_end   = Button(392, 56, 86, 30, "Set End")
        self.btn_clear     = Button(484, 56, 86, 30, "Clear")
        for b in (self.btn_set_start, self.btn_set_end, self.btn_clear):
            b.set_font(self.f_sm)

        self.placing_mode = None

    def handle_event(self, event, app):
        if self.tab_sort.handle_event(event): self._switch("sorting", app)
        if self.tab_path.handle_event(event): self._switch("pathfinding", app)
        if self.dropdown.handle_event(event):
            self.state.algo_index = self.dropdown.selected; app.reset()

        if self.btn_start.handle_event(event):  app.start()
        if self.btn_pause.handle_event(event):  app.toggle_pause()
        if self.btn_reset.handle_event(event):  app.reset()
        if self.btn_random.handle_event(event): app.randomise_array()

        if self.btn_set_start.handle_event(event):
            self.placing_mode = "start"
            self.state.status_msg = "Click a grid cell to place Start"
        if self.btn_set_end.handle_event(event):
            self.placing_mode = "end"
            self.state.status_msg = "Click a grid cell to place End"
        if self.btn_clear.handle_event(event):
            app.reset_grid(); self.placing_mode = None

        self.slider.handle_event(event)
        self.state.speed = self.slider.value

        if self.state.mode == "sorting" and not self.state.running:
            if self.state.is_search_algo:
                # Target input
                r = self.target_input.handle_event(event)
                if r is not None: self._apply_target(r)
                if self.btn_set_target.handle_event(event):
                    p = self.target_input._parse()
                    if p is not None: self._apply_target(p)
                    else: self._set_msg("Enter a valid number!", (255,69,58))
            else:
                # Array input
                r = self.array_input.handle_event(event)
                if r is not None: self._apply_custom_array(r, app)
                if self.btn_apply.handle_event(event):
                    p = self.array_input._parse()
                    if p is not None: self._apply_custom_array(p, app)
                    else: self._set_msg("Invalid! Use numbers 1-200, max 50", (255,69,58))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.dropdown.rect.collidepoint(event.pos):
                self.dropdown.open = False

    def _apply_custom_array(self, values, app):
        app.reset()
        self.state.array = values
        self.state.bar_count = len(values)
        app.sort_view.reset_states()
        self._set_msg(f"Applied! {len(values)} elements", C_GREEN)

    def _apply_target(self, val):
        self.state.search_target = val
        self._set_msg(f"Target set to {val} — press Start", C_CYAN)

    def _set_msg(self, msg, col):
        self.input_msg = msg; self.input_msg_col = col; self.input_msg_timer = 150

    def _switch(self, mode, app):
        self.state.mode = mode
        self.state.algo_index = 0
        self.dropdown.options  = self.state.algo_list
        self.dropdown.selected = 0
        self.tab_sort.pressed = (mode == "sorting")
        self.tab_path.pressed = (mode == "pathfinding")
        self.placing_mode = None
        app.reset()

    def update(self, mouse_pos):
        for w in (self.tab_sort, self.tab_path, self.dropdown,
                  self.btn_start, self.btn_pause, self.btn_reset, self.btn_random,
                  self.btn_set_start, self.btn_set_end, self.btn_clear,
                  self.btn_apply, self.btn_set_target):
            w.update(mouse_pos)
        self.array_input.update()
        self.target_input.update()

        if self.input_msg_timer > 0:
            self.input_msg_timer -= 1
            if self.input_msg_timer == 0: self.input_msg = ""

        running  = self.state.running
        finished = self.state.finished
        paused   = self.state.paused

        self.btn_start.enabled     = not running or finished
        self.btn_pause.enabled     = running and not finished
        self.btn_pause.label       = "Resume" if paused else "Pause"
        self.btn_random.enabled    = self.state.mode == "sorting" and not running
        self.btn_set_start.enabled = not running
        self.btn_set_end.enabled   = not running
        self.btn_clear.enabled     = not running
        self.btn_apply.enabled     = (self.state.mode == "sorting"
                                      and not running
                                      and not self.state.is_search_algo)
        self.btn_set_target.enabled = (self.state.mode == "sorting"
                                       and not running
                                       and self.state.is_search_algo)

    def draw(self, surface):
        pygame.draw.rect(surface, C_PANEL, (0, 0, WIDTH, TOP_PANEL_H))
        pygame.draw.line(surface, C_BORDER, (0, TOP_PANEL_H), (WIDTH, TOP_PANEL_H), 1)

        t = self.f_title.render("AlgoViz", True, C_CYAN)
        surface.blit(t, (WIDTH - t.get_width() - 16, 10))
        s = self.f_sub.render("Desktop Edition", True, C_TEXT_DIM)
        surface.blit(s, (WIDTH - s.get_width() - 16, 36))

        for text, x in (("MODE", 16), ("ALGORITHM", 300), ("CONTROLS", 496)):
            l = self.f_sub.render(text, True, C_TEXT_MUTED)
            surface.blit(l, (x, 4))

        pygame.draw.line(surface, C_BORDER, (288, 10), (288, TOP_PANEL_H - 10))
        pygame.draw.line(surface, C_BORDER, (484, 10), (484, TOP_PANEL_H - 10))

        self.tab_sort.draw(surface)
        self.tab_path.draw(surface)
        self.dropdown.draw(surface)
        self.btn_start.draw(surface)
        self.btn_pause.draw(surface)
        self.btn_reset.draw(surface)

        if self.state.mode == "sorting":
            self.btn_random.draw(surface)

            if self.state.is_search_algo:
                # Search algo — target input দেখাই
                lbl = self.f_hint.render("SEARCH TARGET VALUE:", True, C_TEXT_MUTED)
                surface.blit(lbl, (582, 50))
                self.target_input.draw(surface)
                self.btn_set_target.draw(surface)
                # Current target
                if self.state.search_target is not None:
                    cur = self.f_sm.render(
                        f"Current target: {self.state.search_target}",
                        True, (255, 214, 10))
                    surface.blit(cur, (786, 62))
            else:
                # Normal sort — array input দেখাই
                lbl = self.f_hint.render("CUSTOM ARRAY (comma-sep, 1-200, max 50):", True, C_TEXT_MUTED)
                surface.blit(lbl, (582, 50))
                self.array_input.draw(surface)
                self.btn_apply.draw(surface)

            if self.input_msg:
                msg_s = self.f_sm.render(self.input_msg, True, self.input_msg_col)
                surface.blit(msg_s, (582, 90))
            else:
                if self.state.is_search_algo:
                    h = self.f_hint.render(
                        "Type a number & Set target, then press Start",
                        True, C_TEXT_MUTED)
                else:
                    h = self.f_hint.render(
                        "Type values & Enter/Apply  |  Random = new array",
                        True, C_TEXT_MUTED)
                surface.blit(h, (582, 90))
        else:
            self.btn_set_start.draw(surface)
            self.btn_set_end.draw(surface)
            self.btn_clear.draw(surface)
            if self.placing_mode:
                col = C_GREEN if self.placing_mode == "start" else C_ORANGE
                pm  = self.f_sm.render(
                    f"Placing {self.placing_mode.upper()} — click a cell", True, col)
                surface.blit(pm, (300, 92))

        self.slider.draw(surface)
