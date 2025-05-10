Problem Statement

Given the following unsorted array, sort it in ascending order using the Selection Sort algorithm:

Input: [29, 10, 14, 37, 13]
Solution (Step-by-Step Execution)
Step 1: Find the smallest element in the unsorted part and swap it with the first unsorted element.

    Initial Array: [29, 10, 14, 37, 13]

    Smallest in unsorted part (index 0 to 4): 10 (at index 1)

    Swap 29 (index 0) and 10 (index 1)

    Array after 1st pass: [10, 29, 14, 37, 13]

Step 2: Repeat for the remaining unsorted part (index 1 to 4).

    Smallest in unsorted part (index 1 to 4): 13 (at index 4)

    Swap 29 (index 1) and 13 (index 4)

    Array after 2nd pass: [10, 13, 14, 37, 29]

Step 3: Next smallest in unsorted part (index 2 to 4).

    Smallest in unsorted part (index 2 to 4): 14 (already at correct position)

    No swap needed

    Array remains: [10, 13, 14, 37, 29]

Step 4: Next smallest in unsorted part (index 3 to 4).

    Smallest in unsorted part (index 3 to 4): 29 (at index 4)

    Swap 37 (index 3) and 29 (index 4)

    Array after final pass: [10, 13, 14, 29, 37]

Final Sorted Array: [10, 13, 14, 29, 37]