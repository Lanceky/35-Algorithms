Problem Statement: Two Pointer Technique

Objective:
Given a sorted array of integers, find if there exists a pair of numbers that sums up to a target value.

Example:

    Input: nums = [1, 2, 3, 4, 6], target = 8

    Output: True (since 2 + 6 = 8)

Procedure for Solving Using Two Pointers

    Initialize Pointers:

        left at the start (0).

        right at the end (len(nums) - 1).

    Loop Until Pointers Meet:

        Calculate the sum of nums[left] + nums[right].

        If sum == target, return True.

        If sum < target, move left forward (to increase sum).

        If sum > target, move right backward (to decrease sum).

    Return False if No Pair Found:

        If pointers cross (left >= right), no solution exists.