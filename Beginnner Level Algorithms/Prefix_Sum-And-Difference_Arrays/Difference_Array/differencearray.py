def apply_range_updates(arr, updates):
    n = len(arr)
    diff = [0] * n
    diff[0] = arr[0]
    for i in range(1, n):
        diff[i] = arr[i] - arr[i - 1]

    for l, r, x in updates:
        diff[l] += x
        if r + 1 < n:
            diff[r + 1] -= x

    # Reconstruct the array
    res = [0] * n
    res[0] = diff[0]
    for i in range(1, n):
        res[i] = res[i - 1] + diff[i]
    return res


# Example Usage
arr = [1, 2, 3, 4, 5]
updates = [(1, 3, 2), (2, 4, -1)]  # (l, r, x)
print(apply_range_updates(arr, updates))  # Output: [1, 4, 4, 5, 4]