Problem Statement: Find the Kth Largest Element in a Stream

Task:
Design a class that efficiently tracks the kth largest element in a stream of integers (numbers received one by one). After each new number, return the current kth largest element.

Constraints:

    1 ≤ k ≤ 10^4

    Numbers are added one at a time (streaming data).

    At least k elements will be in the stream when queried.

Example:
python

kth_largest = KthLargest(3, [4, 5, 8, 2])
kth_largest.add(3)   # Returns 4 (sorted: [2, 3, 4, 5, 8])
kth_largest.add(5)   # Returns 5 (sorted: [2, 3, 4, 5, 5, 8])
kth_largest.add(10)  # Returns 5 (sorted: [2, 3, 4, 5, 5, 8, 10])

Solution Using a Min-Heap (Priority Queue)
Why a Min-Heap?

    Efficiency: Maintains the top k elements in O(log k) time per insertion.

    Space Optimization: Only stores k elements (O(k) space).

Python Implementation
python

import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        """
        Initialize with a min-heap of the k largest elements.
        - Time: O(n log k) to heapify initial elements.
        - Space: O(k)
        """
        self.k = k
        self.min_heap = nums[:]
        heapq.heapify(self.min_heap)  # Convert list to heap
        
        # Keep only the k largest elements
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)  # Pop smallest

    def add(self, val: int) -> int:
        """
        Add new value and return the kth largest.
        - Time: O(log k) for insertion/heapop.
        """
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)  # Maintain heap size
        return self.min_heap[0]  # Root = kth largest

Key Steps Explained

    Initialization (__init__):

        Convert input list into a min-heap.

        Trim the heap to size k by repeatedly removing the smallest elements.

    Adding Elements (add):

        Push the new value into the heap.

        If heap size exceeds k, remove the smallest element.

        The root of the heap is always the kth largest element.

Time & Space Complexity
Operation	Time Complexity	Space Complexity
__init__	O(n log k)	O(k)
add	O(log k)	O(k)
Why This Works

    The min-heap tracks the top k elements seen so far.

    The smallest in this heap (root) is the kth largest overall.

    Example Walkthrough:

        Initial heap (k=3): [4, 5, 8] → root = 4 (3rd largest).

        Add 3 → heap becomes [4, 5, 8] → still 4.

        Add 5 → heap becomes [5, 5, 8] → root = 5.

Real-World Applications

    Stock Market: Track the top k portfolio performers.

    Network Monitoring: Identify the k most frequent IP addresses.

    Gaming Leaderboards: Maintain top k scores efficiently.


Heap Data Structure and Priority Queues: A Complete Guide
1. What is a Heap?

A heap is a specialized tree-based data structure that satisfies the heap property:

    In a min-heap, every parent node is less than or equal to its children.

    In a max-heap, every parent node is greater than or equal to its children.

Key Characteristics

    Complete Binary Tree: All levels are fully filled except possibly the last, which is filled left-to-right.

    Efficient Operations: Insertion and extraction take O(log n) time.

    No Order Between Siblings: Unlike BSTs, heaps only enforce parent-child relationships.

2. Heap Operations & Time Complexity
Operation	Time Complexity	Description
Insert	O(log n)	Add new element while maintaining heap property
Extract-Min/Max	O(log n)	Remove and return root (min/max)
Peek (Min/Max)	O(1)	View root without removal
Heapify	O(n)	Convert array into heap
Delete Arbitrary	O(log n)	Remove specific element (requires search)
3. Priority Queues

A priority queue is an abstract data type (ADT) that operates similarly to a heap:

    Always processes the highest/lowest priority element first.

    Common Implementations:

        Binary Heap (most common)

        Fibonacci Heap (advanced, for graph algorithms)

        Python’s heapq / Java’s PriorityQueue

Priority Queue Operations
python

from queue import PriorityQueue

pq = PriorityQueue()
pq.put((priority, data))  # Insert (O(log n))
print(pq.get())           # Extract min-priority (O(log n))

4. How Heaps Work (Step-by-Step)
A. Insertion (O(log n))

    Add element at the next available position (maintaining complete tree structure).

    "Bubble Up" (Heapify-Up):

        Compare with parent.

        If violates heap property (e.g., child < parent in min-heap), swap.

        Repeat until heap property is restored.

Example (Min-Heap Insert 2):

Initial:     3           After Insert 2:     2
            / \                            /   \
           5   4                          3     4
                                        /
                                       5

B. Extraction (O(log n))

    Remove root (min/max element).

    Move last element to root.

    "Bubble Down" (Heapify-Down):

        Compare with children.

        Swap with smaller (min-heap) or larger (max-heap) child.

        Repeat until heap property is restored.

Example (Extract-Min):

Before:     2           After Extraction:     3
           / \                              /   \
          3   4                            5     4
         /
        5

5. Practical Applications
Use Case	Why Heap?
Dijkstra’s Algorithm	Efficiently fetch next closest node
Huffman Coding	Build optimal prefix codes
Job Scheduling	Execute highest-priority tasks first
Merge K Sorted Lists	Always merge smallest next element
Top-K Elements	Maintain heap of size K (O(n log k))
6. Heap vs. Sorted Array
Metric	Heap	Sorted Array
Insert	O(log n)	O(n)
Extract-Min	O(log n)	O(1)
Build	O(n)	O(n log n)
Search	O(n)	O(log n)
Best For	Dynamic data	Static data
7. Code Implementation (Python)
Min-Heap with heapq
python

import heapq

heap = []
heapq.heappush(heap, 3)  # Insert
heapq.heappush(heap, 1)
print(heapq.heappop(heap))  # Extract-min → 1

Max-Heap Trick
python

max_heap = []
heapq.heappush(max_heap, -3)  # Store negatives
heapq.heappush(max_heap, -1)
print(-heapq.heappop(max_heap))  → 3 (original max)

Heapify (Convert List to Heap)
python

arr = [3, 1, 2]
heapq.heapify(arr)  # O(n)

8. Advanced Topics
A. Heap Sort

    Build max-heap from array (O(n)).

    Repeatedly extract max and place at end (O(n log n)).

    Result: Sorted array in-place.

B. K-th Largest Element

    Optimal Approach: Maintain min-heap of size K → O(n log k).

C. Custom Comparators (Java/C++)
java

// Max-heap in Java
PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

