def bubble_sort_steps(arr):
    """Generate step-by-step animation data for bubble sort."""
    a = list(arr)
    n = len(a)
    steps = []

    for i in range(n):
        for j in range(0, n - i - 1):
            sorted_indices = list(range(n - i, n))
            steps.append({
                "array": list(a),
                "active": j,
                "compared": j + 1,
                "sorted": sorted_indices,
                "code_line": 3,
                "text": f"Comparing {a[j]} and {a[j+1]}"
            })
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                steps.append({
                    "array": list(a),
                    "active": j + 1,
                    "compared": j,
                    "sorted": sorted_indices,
                    "code_line": 7,
                    "text": f"Swapped! {a[j+1]} > {a[j]}"
                })
        sorted_indices = list(range(n - i - 1, n))
        steps.append({
            "array": list(a),
            "active": -1,
            "compared": -1,
            "sorted": sorted_indices,
            "code_line": 2,
            "text": f"Pass {i+1} done. Element {a[n-1-i]} is in final position."
        })

    steps.append({
        "array": list(a),
        "active": -1,
        "compared": -1,
        "sorted": list(range(n)),
        "code_line": 8,
        "text": "Array is fully sorted!"
    })
    return steps
