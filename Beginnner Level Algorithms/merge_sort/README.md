Problem Statement: Merge Sort

Objective:
Given an unsorted array of n elements, write a program to sort the array in ascending order using the Merge Sort algorithm.

Input:
An array arr of integers, e.g., [38, 27, 43, 3, 9, 82, 10].

Output:
The sorted array in ascending order, e.g., [3, 9, 10, 27, 38, 43, 82].
Detailed Procedure for Merge Sort
1. Overview of Merge Sort

Merge Sort is a divide-and-conquer algorithm that works as follows:

    Divide the unsorted array into two halves.

    Recursively sort each half.

    Merge the two sorted halves into a single sorted array.

It has a time complexity of O(n log n) in all cases (best, average, worst) and uses O(n) auxiliary space.
2. Step-by-Step Procedure
Step 1: Divide the Array

    If the array has only one element, it is already sorted.

    Otherwise, split the array into two roughly equal subarrays.

Example:
For arr = [38, 27, 43, 3, 9, 82, 10],

    First split: [38, 27, 43, 3] and [9, 82, 10]

    Recursively split until single elements remain.

Step 2: Recursively Sort Subarrays

    Keep dividing until subarrays have only one element.

    Then, start merging them back in sorted order.

Step 3: Merge Two Sorted Subarrays

    Compare elements from both subarrays one by one.

    Place the smaller element into the merged array.

    If one subarray is exhausted, append the remaining elements from the other.

Example of Merging:
Suppose we have two sorted subarrays:

    L = [27, 38]

    R = [3, 43]

Merging Process:

    Compare L[0] (27) and R[0] (3) → Take 3 → Merged: [3]

    Compare L[0] (27) and R[1] (43) → Take 27 → Merged: [3, 27]

    Compare L[1] (38) and R[1] (43) → Take 38 → Merged: [3, 27, 38]

    Append remaining 43 → Final merged: [3, 27, 38, 43]

3. Pseudocode Implementation
python

def merge_sort(arr):
    if len(arr) > 1:
        # Step 1: Divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Step 2: Recursively sort each half
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Step 3: Merge the two sorted halves
        i = j = k = 0  # i for left, j for right, k for merged array
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Append remaining elements (if any)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

4. Example Walkthrough

Input: [38, 27, 43, 3, 9, 82, 10]

Step-by-Step Execution:

    Split into [38, 27, 43, 3] and [9, 82, 10]

    Split [38, 27, 43, 3] into [38, 27] and [43, 3]

        Split [38, 27] into [38] and [27] → Merge → [27, 38]

        Split [43, 3] into [43] and [3] → Merge → [3, 43]

        Merge [27, 38] and [3, 43] → [3, 27, 38, 43]

    Split [9, 82, 10] into [9] and [82, 10]

        Split [82, 10] into [82] and [10] → Merge → [10, 82]

        Merge [9] and [10, 82] → [9, 10, 82]

    Merge [3, 27, 38, 43] and [9, 10, 82] → [3, 9, 10, 27, 38, 43, 82]

Final Output: [3, 9, 10, 27, 38, 43, 82]
Key Takeaways

    Merge Sort is stable (preserves order of equal elements).

    It is not in-place (requires extra space for merging).

    Well-suited for linked lists (efficient merging without extra space).