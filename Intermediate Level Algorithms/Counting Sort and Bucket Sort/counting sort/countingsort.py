def counting_sort(arr):
    # Find range of scores (0 to 100)
    max_score = 100
    min_score = 0
    range_size = max_score - min_score + 1

    # Initialize count array
    count = [0] * range_size

    # Count occurrences of each score
    for score in arr:
        count[score - min_score] += 1

    # Calculate cumulative counts
    for i in range(1, range_size):
        count[i] += count[i - 1]

    # Build sorted output
    output = [0] * len(arr)
    for score in reversed(arr):  # Maintain stability
        output[count[score - min_score] - 1] = score
        count[score - min_score] -= 1

    return output


# Test
scores = [78, 92, 64, 92, 85, 78, 100]
print(counting_sort(scores))  # [64, 78, 78, 85, 92, 92, 100]