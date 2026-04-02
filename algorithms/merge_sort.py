# =============================================================================
# algorithms/merge_sort.py
# ------------------------
# Merge Sort algorithm — generator function দিয়ে বানানো।
#
# কিভাবে কাজ করে:
#   1. Array কে অর্ধেক অর্ধেক করে ভাগ করে (Divide)
#   2. প্রতিটি অর্ধেক recursively sort করে
#   3. দুটো sorted অর্ধেক merge করে একটি sorted array বানায় (Conquer)
#
# Time:  সবসময় O(n log n) — সেরা performance
# Space: O(n) — extra array লাগে merge করার জন্য
# =============================================================================

def merge_sort(arr):
    """
    Merge Sort generator।
    সরাসরি yield করা যায় না কারণ recursive — তাই আগে steps collect করি,
    তারপর একে একে yield করি।
    """
    a = list(arr)
    steps = []
    _collect(a, 0, len(a) - 1, steps)  # সব steps collect করি

    for s in steps:
        yield s  # একে একে visualizer কে দিই

    # সম্পূর্ণ sorted হয়ে গেছে
    yield {
        "arr": list(a),
        "highlights": {k: "sorted" for k in range(len(a))},
        "swap": False, "done": True, "stat": None,
        "info": "Merge Sort complete!"
    }


def _collect(a, l, r, steps):
    """
    Recursive helper — array কে ভাগ করে এবং merge করে।
    সব animation steps একটি list এ জমা করে।
    """
    if l >= r:
        return  # একটি element — এটি already sorted

    m = (l + r) // 2  # মাঝের index

    # Splitting দেখাচ্ছি
    steps.append({
        "arr": list(a),
        "highlights": {k: "active" for k in range(l, r + 1)},
        "swap": False, "done": False, "stat": None,
        "info": f"Splitting [{l}..{r}] into [{l}..{m}] and [{m+1}..{r}]"
    })

    _collect(a, l, m, steps)       # বাম অর্ধেক sort করো
    _collect(a, m + 1, r, steps)   # ডান অর্ধেক sort করো
    _merge(a, l, m, r, steps)      # দুটো মিলিয়ে দাও


def _merge(a, l, m, r, steps):
    """
    দুটো sorted অংশ একসাথে merge করে।
    বাম: a[l..m]  ডান: a[m+1..r]
    """
    left  = a[l: m + 1]    # বাম অংশের copy
    right = a[m + 1: r + 1] # ডান অংশের copy
    i = j = 0
    k = l

    while i < len(left) and j < len(right):
        # দুই দিকের ছোটটি নেব
        steps.append({
            "arr": list(a),
            "highlights": {l + i: "active", m + 1 + j: "compared"},
            "swap": False, "done": False, "stat": "compare",
            "info": f"Comparing {left[i]} and {right[j]}"
        })

        if left[i] <= right[j]:
            a[k] = left[i]; i += 1
        else:
            a[k] = right[j]; j += 1

        steps.append({
            "arr": list(a),
            "highlights": {k: "swap"},
            "swap": True, "done": False, "stat": "swap",
            "info": f"Placed {a[k]} at index {k}"
        })
        k += 1

    # বাকি elements গুলো সরাসরি রেখে দাও
    while i < len(left):  a[k] = left[i];  i += 1; k += 1
    while j < len(right): a[k] = right[j]; j += 1; k += 1

    steps.append({
        "arr": list(a),
        "highlights": {idx: "active" for idx in range(l, r + 1)},
        "swap": False, "done": False, "stat": None,
        "info": f"Merged segment [{l}..{r}] successfully"
    })
