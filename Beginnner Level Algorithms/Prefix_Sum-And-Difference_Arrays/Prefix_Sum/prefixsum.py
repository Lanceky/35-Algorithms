def compute_prefix_sum(arr):
    n = len(arr)
    prefix = [0] * (n + 1)  # Initialize prefix array with 0s (size n+1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]  # Cumulative sum at each step
    return prefix  # Return computed prefix array

def range_sum_query(prefix, l, r):
    # Query formula: sum[l..r] = prefix[r+1] - prefix[l]
    return prefix[r + 1] - prefix[l]

# Example Usage
arr = [1, 3, 2, 5, 4]  # Input array
prefix = compute_prefix_sum(arr)  # Preprocess prefix sums
print(range_sum_query(prefix, 1, 3))  # Output: 10 (sum of 3+2+5)