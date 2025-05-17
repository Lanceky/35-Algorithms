def contains_duplicate(nums):
    """
    Checks if the list contains duplicate elements.

    Args:
    nums (list): List of integers.

    Returns:
    bool: True if duplicates exist, False otherwise.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Test cases
print(contains_duplicate([1, 2, 3, 4]))  # Output: False
print(contains_duplicate([1, 2, 3, 1]))  # Output: True
