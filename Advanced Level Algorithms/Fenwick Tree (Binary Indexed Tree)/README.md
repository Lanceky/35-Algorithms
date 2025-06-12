1. What is a Fenwick Tree?

A Fenwick Tree (or Binary Indexed Tree, BIT) is a space-efficient data structure that supports:

    Prefix sum queries in O(log n) time.

    Point updates in O(log n) time.

It is particularly useful for dynamic frequency tables and cumulative sum problems where the array is frequently updated.
Key Features

    Efficiency: Faster than prefix sum arrays (which take O(n) for updates).

    Space: Uses O(n) space (same as the input array).

    Operations:

        update(i, delta): Add delta to A[i] in O(log n).

        query(i): Get sum A[0] + A[1] + ... + A[i] in O(log n).

2. Why Use a Fenwick Tree?
Applications

    Dynamic Range Sum Queries

        Example: Stock price updates and cumulative sums.

    Inversion Count in Arrays

        Used in algorithms like Merge Sort for counting inversions.

    Frequency Tables

        Efficiently track frequencies and compute prefix sums.

    Competitive Programming

        Problems requiring efficient point updates and prefix queries.

Comparison with Alternatives
Data Structure	Prefix Query	Point Update	Space
Prefix Sum Array	O(1)	O(n)	O(n)
Segment Tree	O(log n)	O(log n)	O(4n)
Fenwick Tree	O(log n)	O(log n)	O(n)

→ Fenwick Tree is optimal when you need both fast updates and prefix queries.
3. How Fenwick Tree Works
Key Idea: Binary Representation

    Each index i in the Fenwick Tree stores a partial sum of a range.

    The range is determined by the least significant bit (LSB) of i.

LSB Trick

    The LSB of i determines how much it "covers":

        i = 6 (110) → LSB = 2 → Covers A[5..6].

        i = 8 (1000) → LSB = 8 → Covers A[1..8].

Operations

    Update (i, delta)

        Propagate the update to all affected indices by adding LSB.
    python

while i <= n:
    BIT[i] += delta
    i += (i & -i)  # Move to next covering index

Query (i)

    Sum all partial sums by subtracting LSB.

python

    res = 0
    while i > 0:
        res += BIT[i]
        i -= (i & -i)  # Move to parent index
    return res

