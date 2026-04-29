from core.constants import SPEED_DEFAULT, BAR_COUNT_DEFAULT


class AppState:
    SORTING_ALGOS = [
        "Bubble Sort", "Selection Sort", "Merge Sort",
        "Insertion Sort", "Quick Sort",
        "Binary Search", "Linear Search",
    ]
    PATH_ALGOS = ["BFS", "Dijkstra", "DFS"]

    # Search algorithms — এগুলোর জন্য target value লাগে
    SEARCH_ALGOS = {"Binary Search", "Linear Search"}

    def __init__(self):
        self.mode       = "sorting"
        self.algo_index = 0

        self.running    = False
        self.paused     = False
        self.finished   = False
        self.speed      = SPEED_DEFAULT
        self.step_timer = 0
        self.generator  = None

        self.bar_count   = BAR_COUNT_DEFAULT
        self.array       = []
        self.bar_states  = {}
        self.comparisons = 0
        self.swaps       = 0

        # Search target value
        self.search_target = None

        self.grid         = None
        self.start_cell   = None
        self.end_cell     = None
        self.path_length  = 0
        self.nodes_visited = 0

        self.status_msg  = "Ready"
        self.fps_display = 60

    @property
    def algo_list(self):
        return self.SORTING_ALGOS if self.mode == "sorting" else self.PATH_ALGOS

    @property
    def algo_name(self):
        return self.algo_list[self.algo_index]

    @property
    def is_search_algo(self):
        return self.algo_name in self.SEARCH_ALGOS

    @property
    def steps_per_frame(self):
        if self.speed >= 9: return 4
        if self.speed >= 8: return 2
        return 1

    @property
    def delay_frames(self):
        delays = {1: 40, 2: 28, 3: 18, 4: 12, 5: 8, 6: 4, 7: 2}
        return delays.get(self.speed, 0)

    def reset_stats(self):
        self.comparisons   = 0
        self.swaps         = 0
        self.path_length   = 0
        self.nodes_visited = 0

    def stop(self):
        self.running    = False
        self.paused     = False
        self.finished   = False
        self.generator  = None
        self.step_timer = 0
