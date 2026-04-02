# =============================================================================
# algorithms/__init__.py
# ----------------------
# Algorithm Registry — সব algorithm এখানে register করা।
# নতুন algorithm যোগ করতে হলে:
#   1. algorithms/ ফোল্ডারে নতুন .py file বানাও
#   2. এখানে import করো
#   3. SORTING_REGISTRY বা PATH_REGISTRY তে যোগ করো
# =============================================================================

from algorithms.bubble_sort    import bubble_sort
from algorithms.selection_sort import selection_sort
from algorithms.merge_sort     import merge_sort
from algorithms.bfs            import bfs
from algorithms.dijkstra       import dijkstra

# Sorting algorithms — নাম: function
SORTING_REGISTRY = {
    "Bubble Sort":    bubble_sort,
    "Selection Sort": selection_sort,
    "Merge Sort":     merge_sort,
}

# Pathfinding algorithms — নাম: function
PATH_REGISTRY = {
    "BFS":      bfs,
    "Dijkstra": dijkstra,
}
