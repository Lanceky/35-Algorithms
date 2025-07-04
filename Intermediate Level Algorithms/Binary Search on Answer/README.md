Binary Search on Answer: Advanced Problem Solving
1. Concept Explanation

Binary Search on Answer is a powerful technique where we:
  
    Identify a search space (possible answers)

    Define a validation function (checks if a candidate answer works)

    Use binary search to efficiently find the optimal solution

When to Use This?

    When the problem asks for minimum/maximum of some value

    When brute force is too slow but verification is fast

    Problems like:

        Capacity to ship packages

        Minimum time to complete tasks

        Maximum allocation of resources

2. Real-World Analogy: Shipping Container Loading

Imagine you're a dock manager who needs to:

    Determine the smallest truck capacity that can ship all packages within D days

    Constraints:

        Packages must be shipped in order

        Can't split a package across trucks

    Binary Search Approach:

        Search space: Max package weight → Total sum of weights

        For each candidate capacity, simulate loading trucks

        Adjust search range based on whether it's possible

3. Problem Statement: Minimum Capacity to Ship Packages

Given:

    weights: Array of package weights (e.g., [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    days: Maximum shipping days (e.g., 5)

Find: The minimum truck capacity needed to ship all packages within days.

Example:
python

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15  # Explanation:
            # Day 1: 1,2,3,4,5 (sum=15)
            # Day 2: 6,7 (sum=13)
            # Day 3: 8 (sum=8)
            # Day 4: 9 (sum=9)
            # Day 5: 10 (sum=10)