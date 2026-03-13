def quick_sort_steps(arr):
    steps = []
    a = list(arr)

    def partition(low, high):
        pivot = a[high]
        steps.append({
            "array": list(a), "active": high, "compared": -1, "sorted": [],
            "code_line": 7, "text": f"Pivot = {pivot} (index {high})"
        })
        i = low - 1
        for j in range(low, high):
            steps.append({
                "array": list(a), "active": j, "compared": high, "sorted": [],
                "code_line": 9, "text": f"Comparing {a[j]} with pivot {pivot}"
            })
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                steps.append({
                    "array": list(a), "active": i, "compared": j, "sorted": [],
                    "code_line": 12, "text": f"{a[i]} ≤ {pivot} — moved to left partition"
                })
        a[i + 1], a[high] = a[high], a[i + 1]
        steps.append({
            "array": list(a), "active": i + 1, "compared": -1, "sorted": [i + 1],
            "code_line": 13, "text": f"Pivot {pivot} placed at final index {i+1} ✓"
        })
        return i + 1

    def qs(low, high):
        if low < high:
            pi = partition(low, high)
            qs(low, pi - 1)
            qs(pi + 1, high)

    qs(0, len(a) - 1)
    steps.append({
        "array": list(a), "active": -1, "compared": -1,
        "sorted": list(range(len(a))), "code_line": 4, "text": "Quick sort complete!"
    })
    return steps
