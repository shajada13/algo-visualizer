# =============================================================================
# algorithms/bubble_sort.py
# -------------------------
# Bubble Sort algorithm — generator function দিয়ে বানানো।
#
# কিভাবে কাজ করে:
#   - প্রতিটি pass এ পাশাপাশি দুটো element তুলনা করে।
#   - বড়টা যদি আগে থাকে, তাহলে swap করে।
#   - প্রতিটি pass শেষে সবচেয়ে বড় element শেষে চলে যায়।
#
# Time:  Best O(n) | Average O(n²) | Worst O(n²)
# Space: O(1)
# =============================================================================

def bubble_sort(arr):
    """
    Bubble Sort generator।
    প্রতিটি yield একটি animation step — visualizer এটা ধরে ধরে দেখায়।

    yield করা dict এর fields:
      arr        : বর্তমান array এর অবস্থা
      highlights : {index: colour_key} — কোন bar কোন রঙে দেখাবে
      swap       : True হলে এই step এ swap হয়েছে
      done       : True হলে algorithm শেষ
      stat       : 'compare' | 'swap' | None — statistics এর জন্য
      info       : বাংলায় বোঝার জন্য step description
    """
    a = list(arr)
    n = len(a)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            # দুটো পাশাপাশি element তুলনা করছি
            yield {
                "arr": list(a),
                "highlights": {j: "active", j + 1: "compared"},
                "swap": False, "done": False, "stat": "compare",
                "info": f"Comparing a[{j}]={a[j]} and a[{j+1}]={a[j+1]}"
            }

            if a[j] > a[j + 1]:
                # বড়টা আগে আছে — swap করব
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
                yield {
                    "arr": list(a),
                    "highlights": {j: "swap", j + 1: "swap"},
                    "swap": True, "done": False, "stat": "swap",
                    "info": f"Swapped! {a[j+1]} > {a[j]}"
                }

        # এই pass এ শেষের দিকের elements গুলো sorted হয়ে গেছে
        sorted_h = {n - 1 - k: "sorted" for k in range(i + 1)}
        yield {
            "arr": list(a),
            "highlights": sorted_h,
            "swap": False, "done": False, "stat": None,
            "info": f"Pass {i + 1} complete — last {i+1} element(s) sorted"
        }

        # যদি কোনো swap না হয়, array already sorted
        if not swapped:
            break

    # সব শেষ — পুরো array sorted
    yield {
        "arr": list(a),
        "highlights": {k: "sorted" for k in range(n)},
        "swap": False, "done": True, "stat": None,
        "info": "Bubble Sort complete! Array is fully sorted."
    }
