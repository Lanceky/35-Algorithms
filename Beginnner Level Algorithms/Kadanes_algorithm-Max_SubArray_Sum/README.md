Kadane's Algorithm (Maximum Subarray Sum)
Problem Statement

Given an array of integers, find the contiguous subarray (with at least one number) that has the largest sum.

Example:

    Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    Output: 6 (from subarray [4, -1, 2, 1])

Intuition (Simple Explanation)

Kadane’s Algorithm works by tracking two variables as it scans the array:

    current_max: Maximum sum of the subarray ending at the current position.

    global_max: Maximum sum found so far in the entire array.

At each step, decide whether to:

    Extend the current subarray (if adding the current number improves the sum).

    Start a new subarray (if the current number itself is better than the previous sum).

Step-by-Step Procedure

    Initialize:

        current_max = nums[0] (start with the first element).

        global_max = nums[0].

    Loop through the array (from the 2nd element):

        Update current_max = max(nums[i], current_max + nums[i]).

            If current_max + nums[i] is worse than nums[i] alone, reset the subarray.

        Update global_max = max(global_max, current_max).

    Return global_max.

Real-Life Analogy

Imagine you’re a trader tracking daily profits/losses.
You want to find the best consecutive days to hold a stock for maximum profit.
Kadane’s Algorithm answers: "Should I keep holding or start fresh today?"