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