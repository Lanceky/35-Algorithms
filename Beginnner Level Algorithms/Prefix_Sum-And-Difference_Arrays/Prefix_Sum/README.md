1. Prefix Sum (Cumulative Sum Array)
Problem Statement

Given an array of integers, you need to efficiently answer multiple queries about the sum of elements in any subarray (range between indices l and r). A brute-force approach would take O(n) per query, but with prefix sums, we can answer each query in O(1) after O(n) preprocessing.

Example:

    Input Array: [1, 3, 2, 5, 4]

    Query: Sum from index 1 to 3 (i.e., 3 + 2 + 5)

    Expected Output: 10

How Prefix Sum Works

    Preprocessing:

        Construct a prefix array where prefix[i] stores the sum of elements from arr[0] to arr[i-1].

        prefix[0] = 0 (sum of an empty subarray).

        prefix[1] = arr[0]

        prefix[2] = arr[0] + arr[1]

        prefix[3] = arr[0] + arr[1] + arr[2]

        And so on...

    Answering Queries in O(1):

        The sum of elements from index l to r is:
        Sum(l,r)=prefix[r+1]−prefix[l]
        Sum(l,r)=prefix[r+1]−prefix[l]

Example Calculation:

    For arr = [1, 3, 2, 5, 4]:

        prefix = [0, 1, 4, 6, 11, 15]

        Sum from l=1 to r=3:
        Sum(1,3)=prefix[4]−prefix[1]=11−1=10
        Sum(1,3)=prefix[4]−prefix[1]=11−1=10

Common Problems Solved

Prefix Sum:

    Subarray sum equals K (Leetcode 560)

    Range sum queries (Leetcode 303)

    Find pivot index (Leetcode 724)

When to use:

    Range sum queries (e.g., "What's the sum between indices l and r?")

    Problems involving cumulative sums (e.g., subarray sums, averages)

Real-life analogy:
Like a running total on a receipt - you can quickly find the total between any two items by subtracting line items.