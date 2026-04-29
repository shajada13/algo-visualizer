# =============================================================================
# algorithms/linear_search.py
# Guide focus: Check elements sequentially, highlight one element at a time
# Visualization: একটার পর একটা bar check হচ্ছে, visited গুলো muted রঙে
# Time: O(n) | Space: O(1)
# =============================================================================

def linear_search(arr, target=None):
    """
    Linear Search generator।
    target না দিলে array এর মাঝের value কে target ধরবে।
    """
    a = list(arr)
    n = len(a)

    if target is None:
        target = a[n // 2]   # মাঝের value কে target ধরছি

    yield {
        "arr": list(a),
        "highlights": {k: "default" for k in range(n)},
        "swap": False, "done": False, "stat": None,
        "info": f"Linear Search: looking for target = {target}"
    }

    visited = set()

    for i in range(n):
        # এই element টা check করছি
        hl = {k: "default" for k in range(n)}
        for k in visited:
            hl[k] = "compared"   # already checked — dim
        hl[i] = "active"         # currently checking — উজ্জ্বল

        yield {
            "arr": list(a), "highlights": hl,
            "swap": False, "done": False, "stat": "compare",
            "info": f"Checking index {i}: a[{i}] = {a[i]} ... is it {target}?"
        }

        if a[i] == target:
            # পেয়ে গেছি!
            found_hl = dict(hl)
            found_hl[i] = "sorted"
            yield {
                "arr": list(a), "highlights": found_hl,
                "swap": False, "done": True, "stat": None,
                "info": f"✓ Found {target} at index {i}! Checked {i+1} element(s)."
            }
            return

        visited.add(i)

    # পুরো array check করলাম, পেলাম না
    yield {
        "arr": list(a),
        "highlights": {k: "compared" for k in range(n)},
        "swap": False, "done": True, "stat": None,
        "info": f"✗ {target} not found. All {n} elements checked."
    }
