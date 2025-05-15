def max_subarray(nums):
    if not nums:
        return 0

    current_max = global_max = nums[0]

    for num in nums[1:]:
        current_max = max(num, current_max + num)  # Extend or reset subarray
        global_max = max(global_max, current_max)  # Update best found so far

    return global_max


# Example Usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(nums))  # Output: 6