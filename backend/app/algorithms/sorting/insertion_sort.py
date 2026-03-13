def insertion_sort_steps(arr):
    steps = []
    a = list(arr)
    for i in range(1, len(a)):
        key = a[i]
        steps.append({
            "array": list(a), "active": i, "compared": -1, "sorted": [],
            "code_line": 2, "text": f"Key = {key} at index {i}"
        })
        j = i - 1
        while j >= 0 and a[j] > key:
            steps.append({
                "array": list(a), "active": j + 1, "compared": j, "sorted": [],
                "code_line": 5, "text": f"{a[j]} > {key} — shifting right"
            })
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        steps.append({
            "array": list(a), "active": j + 1, "compared": -1, "sorted": [],
            "code_line": 8, "text": f"Inserted {key} at position {j+1}"
        })
    steps.append({
        "array": list(a), "active": -1, "compared": -1,
        "sorted": list(range(len(a))), "code_line": 9, "text": "Array is fully sorted!"
    })
    return steps


def selection_sort_steps(arr):
    steps = []
    a = list(arr)
    n = len(a)
    for i in range(n):
        min_idx = i
        steps.append({
            "array": list(a), "active": i, "compared": -1, "sorted": list(range(i)),
            "code_line": 3, "text": f"Finding minimum in range [{i}..{n-1}]"
        })
        for j in range(i + 1, n):
            steps.append({
                "array": list(a), "active": min_idx, "compared": j, "sorted": list(range(i)),
                "code_line": 5, "text": f"Comparing current min {a[min_idx]} with {a[j]}"
            })
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        steps.append({
            "array": list(a), "active": i, "compared": -1, "sorted": list(range(i + 1)),
            "code_line": 9, "text": f"Placed {a[i]} at index {i} ✓"
        })
    return steps
