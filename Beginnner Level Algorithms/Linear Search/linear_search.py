from typing import List
class Solution:
    def linearsearch(self, nums: List[int], target: int) -> int:
        """
        Perfom a linear search on the list nums to find target 
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        else:
            return -1

#impementation example
if __name__ == "__main__":
    solution = Solution()
    
    nums = [1,2,3,4,5,6,7,0]
    target = 9
    result  = solution.linearsearch(nums, target)
    print(f"Index of target: {result}")