Sliding Window Technique Explained Simply
Problem:

Given an array of numbers and a fixed window size k, find the maximum sum of any consecutive subarray of size k.

Example:

    Array: [2, 1, 5, 1, 3, 2]

    Window size: k = 3

    Answer: 9 (from [5, 1, 3])

How It Works (Step-by-Step)

    First Window Sum:

        Take the first k numbers ([2, 1, 5]).

        Calculate their sum: 2 + 1 + 5 = 8.

        This is our starting maximum sum (max_sum = 8).

    Slide the Window Forward:

        Move the window right by 1 position (drop 2, add 1).

        New window: [1, 5, 1] → Sum: 1 + 5 + 1 = 7.

        Compare to max_sum (8 > 7 → Keep max_sum = 8).

    Repeat Until the End:

        Next window: [5, 1, 3] → Sum: 5 + 1 + 3 = 9 → New max_sum = 9.

        Next window: [1, 3, 2] → Sum: 1 + 3 + 2 = 6 → max_sum stays 9.

    Final Result:

        The highest sum found is 9.
#summary: 
1. Compute the sum of the first window of size k.
2. Slide the window one element at a time.
3. At each step, subtract the element that is left behind and add the new element.
4. Keep track of the maximum sum encountered.