Concept & Explanation

Bucket Sort distributes elements into buckets based on their values, then sorts each bucket individually. Ideal for uniformly distributed data like floating-point numbers.

Key Properties:

    Average case O(n) when well-distributed

    Can be stable if bucket sorting is stable

    Works best when input is uniformly distributed across range

Real-World Analogy: Mail Sorting System

Imagine a post office sorting letters by zip code ranges:

    Buckets: Bins for different zip code ranges (10000-19999, 20000-29999, etc.)

    Distribution: Mail is placed in appropriate bins

    Sorting: Each bin is sorted individually before delivery

Problem Statement

Sort an array of floating-point numbers uniformly distributed between 0.0 and 1.0.

Input: [0.78, 0.17, 0.39, 0.26, 0.72, 0.94]
Output: [0.17, 0.26, 0.39, 0.72, 0.78, 0.94]