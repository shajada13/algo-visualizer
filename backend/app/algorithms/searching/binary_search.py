def linear_search_steps(arr, target):
    steps = []
    steps.append({
        "array": list(arr), "active": -1, "compared": -1, "sorted": [], "found": -1,
        "code_line": 0, "text": f"Starting linear scan for target = {target}"
    })
    for i in range(len(arr)):
        steps.append({
            "array": list(arr), "active": i, "compared": -1, "sorted": [], "found": -1,
            "code_line": 2, "text": f"Checking index {i}: {arr[i]} == {target}?"
        })
        if arr[i] == target:
            steps.append({
                "array": list(arr), "active": -1, "compared": -1, "sorted": [], "found": i,
                "code_line": 3, "text": f"Found {target} at index {i}!"
            })
            return steps
        steps.append({
            "array": list(arr), "active": -1, "compared": i, "sorted": [], "found": -1,
            "code_line": 1, "text": f"{arr[i]} ≠ {target} — moving on"
        })
    steps.append({
        "array": list(arr), "active": -1, "compared": -1, "sorted": [], "found": -1,
        "code_line": 5, "text": f"{target} not found in array."
    })
    return steps


def binary_search_steps(arr, target):
    steps = []
    sorted_arr = sorted(arr)
    steps.append({
        "array": sorted_arr, "active": -1, "compared": -1, "sorted": [], "found": -1,
        "code_line": 0, "text": f"Array sorted. Searching for {target} using binary search."
    })
    low, high = 0, len(sorted_arr) - 1
    while low <= high:
        mid = (low + high) // 2
        steps.append({
            "array": sorted_arr, "active": mid, "compared": -1,
            "range": [low, high], "sorted": [], "found": -1,
            "code_line": 3, "text": f"Range [{low}..{high}] — midpoint index {mid}: value {sorted_arr[mid]}"
        })
        if sorted_arr[mid] == target:
            steps.append({
                "array": sorted_arr, "active": -1, "compared": -1, "sorted": [], "found": mid,
                "code_line": 4, "text": f"Found {target} at index {mid}!"
            })
            return steps
        elif sorted_arr[mid] < target:
            steps.append({
                "array": sorted_arr, "active": mid, "compared": -1,
                "range": [low, high], "sorted": [], "found": -1,
                "code_line": 6, "text": f"{sorted_arr[mid]} < {target} — search right half"
            })
            low = mid + 1
        else:
            steps.append({
                "array": sorted_arr, "active": mid, "compared": -1,
                "range": [low, high], "sorted": [], "found": -1,
                "code_line": 8, "text": f"{sorted_arr[mid]} > {target} — search left half"
            })
            high = mid - 1
    steps.append({
        "array": sorted_arr, "active": -1, "compared": -1, "sorted": [], "found": -1,
        "code_line": 9, "text": f"{target} not found in array."
    })
    return steps
