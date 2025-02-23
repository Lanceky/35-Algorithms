Problem Statement:

Implement the bubble sort algorithm to sort a list of integers in non-decreasing order. The function should modify the input list in-place and return the sorted list.
Example:
Input: nums = [5, 3, 8, 4, 6]
Output: [3, 4, 5, 6, 8]
Explanation: The list is sorted in non-decreasing order.

#Further explation:
1. An outer loop decrease in size each time.
2. The goal is to have the largest number at the end
   of the llist when the outer loo completes 1 cycle
3. The inner loop starts comparing indexes at the beginning 
    the loop p
4. Check if list[index] = list[index +1]
5. If so swap the index values
6. When the inner loop completes the largest number is at the end of the list
7. Decrement the outer loop by 1