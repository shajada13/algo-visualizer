# =============================================================================
# algorithms/selection_sort.py
# ----------------------------
# Selection Sort algorithm — generator function দিয়ে বানানো।
#
# কিভাবে কাজ করে:
#   - প্রতিটি pass এ unsorted অংশ থেকে সবচেয়ে ছোট element খুঁজে বের করে।
#   - সেটাকে unsorted অংশের শুরুতে রাখে (swap করে)।
#   - প্রতিটি pass এ sorted অংশ একটু বড় হয়।
#
# Time:  সবসময় O(n²) — input যাই হোক
# Space: O(1)
# =============================================================================

def selection_sort(arr):
    """
    Selection Sort generator।
    প্রতিটি yield একটি animation step।
    """
    a = list(arr)
    n = len(a)
    done_set = set()  # যে positions গুলো sorted হয়ে গেছে

    for i in range(n):
        min_idx = i  # ধরে নিচ্ছি i-তম element সবচেয়ে ছোট

        # Minimum খোঁজা শুরু হচ্ছে
        yield {
            "arr": list(a),
            "highlights": {i: "active", **{k: "sorted" for k in done_set}},
            "swap": False, "done": False, "stat": None,
            "info": f"Finding minimum in range [{i}..{n-1}]"
        }

        for j in range(i + 1, n):
            # বর্তমান minimum এর সাথে j-তম element তুলনা করছি
            yield {
                "arr": list(a),
                "highlights": {min_idx: "active", j: "compared",
                               **{k: "sorted" for k in done_set}},
                "swap": False, "done": False, "stat": "compare",
                "info": f"Is a[{j}]={a[j]} smaller than current min={a[min_idx]}?"
            }

            if a[j] < a[min_idx]:
                min_idx = j  # নতুন minimum পেয়েছি

        # Minimum কে সঠিক জায়গায় রাখছি
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            yield {
                "arr": list(a),
                "highlights": {i: "swap", min_idx: "swap",
                               **{k: "sorted" for k in done_set}},
                "swap": True, "done": False, "stat": "swap",
                "info": f"Placed minimum {a[i]} at index {i}"
            }

        done_set.add(i)
        yield {
            "arr": list(a),
            "highlights": {k: "sorted" for k in done_set},
            "swap": False, "done": False, "stat": None,
            "info": f"Position {i} is now finalised"
        }

    # সব শেষ
    yield {
        "arr": list(a),
        "highlights": {k: "sorted" for k in range(n)},
        "swap": False, "done": True, "stat": None,
        "info": "Selection Sort complete!"
    }
