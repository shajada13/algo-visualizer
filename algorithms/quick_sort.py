# =============================================================================
# algorithms/quick_sort.py
# Guide focus: Show pivot selection, show partitioning (left/right regions)
# Visualization: pivot আলাদা রঙে, left region vs right region স্পষ্ট
# Time: Best O(n log n) | Average O(n log n) | Worst O(n²)
# Space: O(log n)
# =============================================================================

def quick_sort(arr):
    a     = list(arr)
    steps = []
    _collect(a, 0, len(a) - 1, steps)
    for s in steps:
        yield s
    yield {
        "arr": list(a),
        "highlights": {k: "sorted" for k in range(len(a))},
        "swap": False, "done": True, "stat": None,
        "info": "Quick Sort complete!"
    }


def _collect(a, lo, hi, steps):
    if lo >= hi:
        if lo == hi:
            steps.append({
                "arr": list(a), "highlights": {lo: "sorted"},
                "swap": False, "done": False, "stat": None,
                "info": f"Single element at index {lo} — already sorted"
            })
        return

    # Pivot হিসেবে শেষ element নিচ্ছি
    pivot     = a[hi]
    pivot_hl  = {k: "default" for k in range(lo, hi + 1)}
    pivot_hl[hi] = "pivot"

    steps.append({
        "arr": list(a),
        "highlights": {**pivot_hl},
        "swap": False, "done": False, "stat": None,
        "info": f"Pivot = {pivot} (index {hi}) | Partitioning [{lo}..{hi}]"
    })

    # Partition — pivot এর চেয়ে ছোট বাম দিকে, বড় ডান দিকে
    i = lo - 1   # smaller region এর শেষ index

    for j in range(lo, hi):
        # বাম অঞ্চল (≤ pivot) এবং ডান অঞ্চল (> pivot) highlight
        hl = {}
        for k in range(lo, i + 1):  hl[k] = "sorted"    # left region (≤ pivot)
        for k in range(i + 1, j):   hl[k] = "compared"  # right region (> pivot)
        hl[j]  = "active"
        hl[hi] = "pivot"

        steps.append({
            "arr": list(a), "highlights": hl,
            "swap": False, "done": False, "stat": "compare",
            "info": f"Is a[{j}]={a[j]} ≤ pivot {pivot}?"
        })

        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
            hl2 = dict(hl)
            hl2[i] = "swap"; hl2[j] = "swap"; hl2[hi] = "pivot"
            steps.append({
                "arr": list(a), "highlights": hl2,
                "swap": True, "done": False, "stat": "swap",
                "info": f"Swapped {a[j]} ↔ {a[i]} (moving {a[i]} to left region)"
            })

    # Pivot কে সঠিক জায়গায় রাখছি
    a[i + 1], a[hi] = a[hi], a[i + 1]
    p = i + 1
    final_hl = {}
    for k in range(lo, p):   final_hl[k] = "sorted"
    final_hl[p] = "pivot"
    for k in range(p + 1, hi + 1): final_hl[k] = "compared"

    steps.append({
        "arr": list(a), "highlights": final_hl,
        "swap": True, "done": False, "stat": "swap",
        "info": f"Pivot {pivot} placed at final index {p} ✓"
    })

    # Recursively দুই দিক sort করো
    _collect(a, lo, p - 1, steps)
    _collect(a, p + 1, hi, steps)
