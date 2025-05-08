def binary_search(nums, target):
    left, right = 0, len(nums)-1  # Initialize search boundaries
    while left <= right:           # Continue while search space is valid
        mid = (left + right) // 2  # Find middle index
        if nums[mid] == target:    # Case 1: Target found
            return mid
        elif nums[mid] < target:   # Case 2: Target is in right half
            left = mid + 1
        else:                      # Case 3: Target is in left half
            right = mid - 1
    return -1                      # Target not found

# Test case
sorted_Arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(sorted_Arr, 9))  # Output: 9