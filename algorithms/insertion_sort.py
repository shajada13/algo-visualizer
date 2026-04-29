# =============================================================================
# algorithms/insertion_sort.py
# Guide focus: Show shifting of elements, show insertion position
# Visualization: "shifting" highlight আলাদা রঙে, insertion point স্পষ্ট
# Time: Best O(n) | Average O(n²) | Worst O(n²)
# Space: O(1)
# =============================================================================

def insertion_sort(arr):
    a = list(arr)
    n = len(a)
    sorted_set = {0}  # প্রথম element শুরু থেকেই sorted

    yield {
        "arr": list(a), "highlights": {0: "sorted"},
        "swap": False, "done": False, "stat": None,
        "info": "Start: first element is trivially sorted"
    }

    for i in range(1, n):
        key = a[i]
        j   = i - 1

        # key element টা তুলে নিচ্ছি — insertion position খুঁজব
        yield {
            "arr": list(a),
            "highlights": {i: "active", **{k: "sorted" for k in sorted_set}},
            "swap": False, "done": False, "stat": None,
            "info": f"Picking key = {key} (index {i}), will find its place"
        }

        # বাম দিকে বড় elements গুলো ডানে সরিয়ে জায়গা বের করছি
        while j >= 0 and a[j] > key:
            yield {
                "arr": list(a),
                "highlights": {j: "compared", j + 1: "swap",
                               **{k: "sorted" for k in sorted_set if k != j}},
                "swap": False, "done": False, "stat": "compare",
                "info": f"Shifting {a[j]} right to make room for {key}"
            }
            a[j + 1] = a[j]   # element টা এক ঘর ডানে সরছে
            yield {
                "arr": list(a),
                "highlights": {j: "active", j + 1: "swap",
                               **{k: "sorted" for k in sorted_set if k != j}},
                "swap": True, "done": False, "stat": "swap",
                "info": f"Shifted {a[j+1]} → index {j+1}"
            }
            j -= 1

        # সঠিক জায়গায় key বসাচ্ছি
        a[j + 1] = key
        sorted_set.add(i)
        yield {
            "arr": list(a),
            "highlights": {j + 1: "pivot", **{k: "sorted" for k in sorted_set}},
            "swap": False, "done": False, "stat": None,
            "info": f"Inserted {key} at index {j+1} ✓"
        }

    yield {
        "arr": list(a),
        "highlights": {k: "sorted" for k in range(n)},
        "swap": False, "done": True, "stat": None,
        "info": "Insertion Sort complete!"
    }
