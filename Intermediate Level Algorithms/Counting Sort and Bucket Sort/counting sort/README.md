1. Counting Sort
Concept & Explanation

Counting Sort is an integer sorting algorithm that works by counting occurrences of each element and using arithmetic to determine positions. It's not comparison-based, making it faster than O(n log n) sorts for constrained inputs.

Key Properties:

    Stable sort (preserves original order of equal elements)

    Works best when input range (k) is small compared to number of elements (n)

    Time Complexity: O(n + k)

    Space Complexity: O(n + k)

Real-World Analogy: Assembly Line Quality Control

Imagine a factory producing screws in sizes 5mm, 10mm, and 15mm:

    Counting: Workers tally screws by size in separate bins

    Positioning: Using counts, screws are placed on conveyor belt in order

    Result: Perfectly sorted output without direct comparisons

Problem Statement

Given an array of student test scores (0 to 100 points), sort them in ascending order.

Input: [78, 92, 64, 92, 85, 78, 100]
Output: [64, 78, 78, 85, 92, 92, 100]