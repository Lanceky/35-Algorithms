Insertion Sort: Complete Refined Explanation
Problem Statement

Given the following unsorted array, sort it in ascending order using the Insertion Sort algorithm:

Input: [12, 11, 13, 5, 6]
Key Concept

    The first element is always considered the initial "sorted" part.

    The algorithm gradually expands the sorted section by inserting one element at a time from the unsorted part into its correct position in the sorted part.

Step-by-Step Execution
Initial Array: [12, 11, 13, 5, 6]

    Sorted part (initially): [12] (first element)

    Unsorted part: [11, 13, 5, 6]

Pass 1: Insert 11 into the Sorted Part

    Key = 11 (first unsorted element).

    Compare 11 with 12 → 11 < 12 → Shift 12 right.

    Insert 11 at index 0.

    Array: [11, 12, 13, 5, 6]

    Sorted part: [11, 12]

Pass 2: Insert 13 into the Sorted Part

    Key = 13.

    Compare 13 with 12 → 13 > 12 → No shift needed.

    Array remains: [11, 12, 13, 5, 6]

    Sorted part: [11, 12, 13]

Pass 3: Insert 5 into the Sorted Part

    Key = 5.

    Compare 5 with 13 → 5 < 13 → Shift 13 right.

    Compare 5 with 12 → 5 < 12 → Shift 12 right.

    Compare 5 with 11 → 5 < 11 → Shift 11 right.

    Insert 5 at index 0 (beginning of the array).

    Array: [5, 11, 12, 13, 6]

    Sorted part: [5, 11, 12, 13]

Pass 4: Insert 6 into the Sorted Part (Corrected)

    Key = 6.

    Compare 6 with 13 → 6 < 13 → Shift 13 right.

    Compare 6 with 12 → 6 < 12 → Shift 12 right.

    Compare 6 with 11 → 6 < 11 → Shift 11 right.

    Compare 6 with 5 → 6 > 5 → Stop shifting.

    Insert 6 at index 1 (after 5).

    Final Sorted Array: [5, 6, 11, 12, 13]

Key Takeaways

✅ First Element is Always Sorted: The algorithm starts with a single-element sorted list and grows it.
✅ Efficiency:

    Best Case (Already Sorted): O(n) (no shifts needed, only comparisons).

    Worst Case (Reverse Sorted): O(n²) (every element shifts to the start).
    ✅ Stable & In-Place: Maintains order of equal elements and uses O(1) extra space.
    ✅ Practical Use: Excellent for small or nearly sorted datasets (e.g., Timsort uses it internally).