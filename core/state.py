# =============================================================================
# core/state.py
# -------------
# Application এর সব data এক জায়গায় রাখা আছে — "Single Source of Truth"।
# যেকোনো জায়গা থেকে এই state পড়া ও লেখা যাবে।
# =============================================================================

from core.constants import SPEED_DEFAULT, BAR_COUNT_DEFAULT


class AppState:
    """
    পুরো app এর state এই class এ।
    Mode, algorithm, array, grid, speed — সব এখানে।
    """

    # Available algorithm list
    SORTING_ALGOS = ["Bubble Sort", "Selection Sort", "Merge Sort"]
    PATH_ALGOS    = ["BFS", "Dijkstra"]

    def __init__(self):
        # --- Mode & Algorithm -------------------------------------------------
        self.mode       = "sorting"      # "sorting" অথবা "pathfinding"
        self.algo_index = 0              # বর্তমান algorithm এর index

        # --- Playback State ---------------------------------------------------
        self.running    = False          # animation চলছে কি না
        self.paused     = False          # pause করা আছে কি না
        self.finished   = False          # algorithm শেষ হয়েছে কি না
        self.speed      = SPEED_DEFAULT  # animation speed (1-10)
        self.step_timer = 0             # frame counter (slow speed এর জন্য)
        self.generator  = None          # active algorithm এর generator

        # --- Sorting Data -----------------------------------------------------
        self.bar_count  = BAR_COUNT_DEFAULT  # কতটি bar দেখাবে
        self.array      = []            # বর্তমান array
        self.bar_states = {}            # {index: 'default'|'active'|'swap'|...}
        self.comparisons = 0            # মোট comparison সংখ্যা
        self.swaps       = 0            # মোট swap সংখ্যা

        # --- Pathfinding Data -------------------------------------------------
        self.grid        = None         # 2D grid (list of lists)
        self.start_cell  = None         # শুরুর cell (row, col)
        self.end_cell    = None         # শেষের cell (row, col)
        self.path_length  = 0           # পাওয়া path এর দৈর্ঘ্য
        self.nodes_visited = 0          # কতটি node visit হয়েছে

        # --- UI ---------------------------------------------------------------
        self.status_msg  = "Ready"      # নিচের status bar এর message
        self.fps_display = 60           # বর্তমান FPS

    # -------------------------------------------------------------------------
    @property
    def algo_list(self):
        """বর্তমান mode অনুযায়ী algorithm list return করে।"""
        return self.SORTING_ALGOS if self.mode == "sorting" else self.PATH_ALGOS

    @property
    def algo_name(self):
        """বর্তমান algorithm এর নাম return করে।"""
        return self.algo_list[self.algo_index]

    @property
    def steps_per_frame(self):
        """প্রতি frame এ কতটি step নেবে (speed বেশি = বেশি step)।"""
        return max(1, self.speed * 2)

    @property
    def delay_frames(self):
        """Slow speed এ দুটো step এর মাঝে কত frame অপেক্ষা করবে।"""
        if self.speed >= 5:
            return 0
        return (5 - self.speed) * 2

    def reset_stats(self):
        """Statistics গুলো শূন্য করে দেয়।"""
        self.comparisons   = 0
        self.swaps         = 0
        self.path_length   = 0
        self.nodes_visited = 0

    def stop(self):
        """Animation সম্পূর্ণ বন্ধ করে দেয়।"""
        self.running    = False
        self.paused     = False
        self.finished   = False
        self.generator  = None
        self.step_timer = 0
