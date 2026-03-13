def merge_sort_steps(arr):
    steps = []
    a = list(arr)

    def merge_sort(arr_slice, offset=0):
        if len(arr_slice) <= 1:
            return arr_slice
        mid = len(arr_slice) // 2
        steps.append({
            "array": list(a),
            "highlight": list(range(offset, offset + len(arr_slice))),
            "active": -1, "compared": -1, "sorted": [],
            "code_line": 3,
            "text": f"Splitting [{', '.join(map(str, arr_slice))}] at index {mid}"
        })
        left = merge_sort(arr_slice[:mid], offset)
        right = merge_sort(arr_slice[mid:], offset + mid)
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
        merged += left[i:] + right[j:]
        for k, v in enumerate(merged):
            a[offset + k] = v
        steps.append({
            "array": list(a),
            "highlight": list(range(offset, offset + len(merged))),
            "active": -1, "compared": -1, "sorted": [],
            "code_line": 16,
            "text": f"Merged → [{', '.join(map(str, merged))}]"
        })
        return merged

    merge_sort(list(arr))
    steps.append({
        "array": sorted(arr),
        "active": -1, "compared": -1,
        "sorted": list(range(len(arr))),
        "code_line": 6,
        "text": "Merge sort complete!"
    })
    return steps
