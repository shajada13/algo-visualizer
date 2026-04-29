from algorithms.bubble_sort     import bubble_sort
from algorithms.selection_sort  import selection_sort
from algorithms.merge_sort      import merge_sort
from algorithms.insertion_sort  import insertion_sort
from algorithms.quick_sort      import quick_sort
from algorithms.binary_search   import binary_search
from algorithms.linear_search   import linear_search
from algorithms.bfs              import bfs
from algorithms.dijkstra         import dijkstra
from algorithms.dfs              import dfs

# Search algorithms এর জন্য wrapper — state থেকে target value নেয়
def _make_search_wrapper(fn):
    def wrapper(arr, target=None):
        return fn(arr, target)
    return wrapper

SORTING_REGISTRY = {
    "Bubble Sort":    bubble_sort,
    "Selection Sort": selection_sort,
    "Merge Sort":     merge_sort,
    "Insertion Sort": insertion_sort,
    "Quick Sort":     quick_sort,
    "Binary Search":  binary_search,
    "Linear Search":  linear_search,
}

PATH_REGISTRY = {
    "BFS":      bfs,
    "Dijkstra": dijkstra,
    "DFS":      dfs,
}
