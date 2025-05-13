Problem Statement

Problem:
Design and implement the Quick Sort algorithm to sort an array of integers in ascending order. Quick Sort is a divide-and-conquer algorithm that partitions an array into sub-arrays, sorts each sub-array, and combines the results to produce the sorted array.
Steps to Solve

    Choose a Pivot Element:
    Select a pivot element from the array. The most common method is to choose the last element as the pivot.

    Example:
    Given the array [10, 7, 8, 9, 1, 5], the pivot is 5.

    Partition the Array:

        Rearrange the elements so that all elements smaller than the pivot are placed to its left and all elements greater are placed to its right.

        The pivot is now in its final sorted position.

    Example:
    After partitioning the array [10, 7, 8, 9, 1, 5] around the pivot 5, we get:

        Smaller elements: [1]

        Pivot: [5]

        Larger elements: [10, 7, 8, 9]

    Recursive Sorting:
    Apply the same logic recursively to the sub-arrays [1] and [10, 7, 8, 9].

    Example:
    Sorting [10, 7, 8, 9] recursively, with 9 as pivot:

        Smaller elements: [7, 8]

        Pivot: [9]

        Larger elements: [10]

    Base Case:
    The recursion stops when the sub-array has one or no elements, as such arrays are already sorted.

    Example:
    The sorted sub-array [7, 8] results from further recursive steps, and combining gives [1, 5, 7, 8, 9, 10].