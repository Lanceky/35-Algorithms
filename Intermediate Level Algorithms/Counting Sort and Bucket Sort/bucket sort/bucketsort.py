def bucket_sort(arr):
    if not arr:
        return arr

    # Create 10 buckets for 0.0-1.0 range
    num_buckets = 10
    buckets = [[] for _ in range(num_buckets)]

    # Distribute elements into buckets
    for num in arr:
        bucket_index = int(num * num_buckets)
        buckets[bucket_index].append(num)

    # Sort individual buckets (using insertion sort)
    sorted_arr = []
    for bucket in buckets:
        # Insertion sort for each bucket
        for i in range(1, len(bucket)):
            key = bucket[i]
            j = i - 1
            while j >= 0 and key < bucket[j]:
                bucket[j + 1] = bucket[j]
                j -= 1
            bucket[j + 1] = key
        sorted_arr.extend(bucket)

    return sorted_arr


# Test
numbers = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94]
print(bucket_sort(numbers))  # [0.17, 0.26, 0.39, 0.72, 0.78, 0.94]