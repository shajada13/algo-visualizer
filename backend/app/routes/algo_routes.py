from flask import Blueprint, jsonify, request

from ..algorithms.sorting.bubble_sort import bubble_sort_steps
from ..algorithms.sorting.insertion_sort import insertion_sort_steps, selection_sort_steps
from ..algorithms.sorting.merge_sort import merge_sort_steps
from ..algorithms.sorting.quick_sort import quick_sort_steps
from ..algorithms.searching.binary_search import binary_search_steps, linear_search_steps
from ..algorithms.graph.bfs import bfs_steps
from ..algorithms.graph.dfs import dfs_steps
from ..algorithms.graph.dijkstra import dijkstra_steps

algo_bp = Blueprint("algo", __name__)

ALGO_META = {
    "bubble_sort":    {"name": "Bubble Sort",    "category": "sorting",   "best": "O(n)", "avg": "O(n²)", "worst": "O(n²)", "space": "O(1)"},
    "insertion_sort": {"name": "Insertion Sort",  "category": "sorting",   "best": "O(n)", "avg": "O(n²)", "worst": "O(n²)", "space": "O(1)"},
    "selection_sort": {"name": "Selection Sort",  "category": "sorting",   "best": "O(n²)","avg": "O(n²)", "worst": "O(n²)", "space": "O(1)"},
    "merge_sort":     {"name": "Merge Sort",      "category": "sorting",   "best": "O(n log n)", "avg": "O(n log n)", "worst": "O(n log n)", "space": "O(n)"},
    "quick_sort":     {"name": "Quick Sort",      "category": "sorting",   "best": "O(n log n)", "avg": "O(n log n)", "worst": "O(n²)", "space": "O(log n)"},
    "linear_search":  {"name": "Linear Search",   "category": "searching", "best": "O(1)", "avg": "O(n)", "worst": "O(n)", "space": "O(1)"},
    "binary_search":  {"name": "Binary Search",   "category": "searching", "best": "O(1)", "avg": "O(log n)", "worst": "O(log n)", "space": "O(1)"},
    "bfs":            {"name": "BFS",             "category": "graph",     "best": "O(V+E)", "avg": "O(V+E)", "worst": "O(V+E)", "space": "O(V)"},
    "dfs":            {"name": "DFS",             "category": "graph",     "best": "O(V+E)", "avg": "O(V+E)", "worst": "O(V+E)", "space": "O(V)"},
    "dijkstra":       {"name": "Dijkstra",        "category": "graph",     "best": "O(E log V)", "avg": "O(E log V)", "worst": "O(E log V)", "space": "O(V)"},
}


@algo_bp.route("/algorithms", methods=["GET"])
def list_algorithms():
    return jsonify(ALGO_META)


@algo_bp.route("/algorithms/<algo_name>", methods=["POST"])
def run_algorithm(algo_name):
    data = request.get_json(silent=True) or {}
    array = data.get("array", [5, 3, 8, 1, 9, 2, 7])
    target = data.get("target", None)

    try:
        steps = _dispatch(algo_name, array, target)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Internal error: {str(e)}"}), 500

    meta = ALGO_META.get(algo_name, {})
    return jsonify({"algorithm": algo_name, "meta": meta, "steps": steps, "total": len(steps)})


def _dispatch(name, array, target):
    match name:
        case "bubble_sort":    return bubble_sort_steps(array)
        case "insertion_sort": return insertion_sort_steps(array)
        case "selection_sort": return selection_sort_steps(array)
        case "merge_sort":     return merge_sort_steps(array)
        case "quick_sort":     return quick_sort_steps(array)
        case "linear_search":  return linear_search_steps(array, target or 0)
        case "binary_search":  return binary_search_steps(array, target or 0)
        case "bfs":            return bfs_steps()
        case "dfs":            return dfs_steps()
        case "dijkstra":       return dijkstra_steps()
        case _:                raise ValueError(f"Unknown algorithm: {name}")
