# =============================================================================
# algorithms/binary_search.py
# Guide focus: Show mid element, shrink search range, fade out eliminated areas
# Visualization: active range স্পষ্ট, eliminated অংশ muted/dim রঙে
# Time: O(log n) | Space: O(1)
# NOTE: Binary Search এর জন্য array sorted হতে হয়।
#       Searching এর target value state থেকে নেওয়া হবে।
# =============================================================================

def binary_search(arr, target=None):
    """
    Binary Search generator।
    target না দিলে array এর মাঝামাঝি value কে target ধরবে।
    """
    a = sorted(arr)   # Binary search sorted array তে হয়
    n = len(a)

    # Target না দেওয়া থাকলে একটা interesting value বেছে নিই
    if target is None:
        target = a[n // 3]   # array এর ১/৩ অবস্থানের value

    lo, hi = 0, n - 1

    # শুরুতে পুরো sorted array দেখাই
    yield {
        "arr": list(a),
        "highlights": {k: "default" for k in range(n)},
        "swap": False, "done": False, "stat": None,
        "info": f"Array is sorted. Searching for target = {target}"
    }

    found = False
    steps = 0

    while lo <= hi:
        mid = (lo + hi) // 2

        # Active range এবং eliminated অংশ আলাদা রঙে দেখাই
        hl = {}
        for k in range(n):
            if k < lo or k > hi:
                hl[k] = "default"   # eliminated — dim রঙে
            elif k == mid:
                hl[k] = "active"    # mid element — উজ্জ্বল
            else:
                hl[k] = "compared"  # active range — normal

        steps += 1
        yield {
            "arr": list(a), "highlights": hl,
            "swap": False, "done": False, "stat": "compare",
            "info": f"Step {steps}: lo={lo}, hi={hi}, mid={mid} → checking a[{mid}]={a[mid]}"
        }

        if a[mid] == target:
            # পেয়ে গেছি!
            found_hl = {k: "default" for k in range(n)}
            found_hl[mid] = "sorted"
            yield {
                "arr": list(a), "highlights": found_hl,
                "swap": False, "done": True, "stat": None,
                "info": f"✓ Found {target} at index {mid}! Took {steps} step(s)."
            }
            found = True
            break
        elif a[mid] < target:
            # Target ডান দিকে — বাম অর্ধেক বাদ
            elim_hl = dict(hl)
            for k in range(lo, mid + 1):
                elim_hl[k] = "default"  # fade out left half
            yield {
                "arr": list(a), "highlights": elim_hl,
                "swap": False, "done": False, "stat": None,
                "info": f"a[{mid}]={a[mid]} < {target} → eliminate LEFT half, search right"
            }
            lo = mid + 1
        else:
            # Target বাম দিকে — ডান অর্ধেক বাদ
            elim_hl = dict(hl)
            for k in range(mid, hi + 1):
                elim_hl[k] = "default"  # fade out right half
            yield {
                "arr": list(a), "highlights": elim_hl,
                "swap": False, "done": False, "stat": None,
                "info": f"a[{mid}]={a[mid]} > {target} → eliminate RIGHT half, search left"
            }
            hi = mid - 1

    if not found:
        yield {
            "arr": list(a),
            "highlights": {k: "default" for k in range(n)},
            "swap": False, "done": True, "stat": None,
            "info": f"✗ {target} not found in array after {steps} step(s)."
        }
