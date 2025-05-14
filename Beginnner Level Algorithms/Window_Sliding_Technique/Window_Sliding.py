def max_subarray_sum(nums, k):
    #Edge case : Array too small
    if len(nums) < k :
        return 0
    #first window sum
    window_sum = sum(nums[:k])
    max_sum = window_sum

    #Slide through the array adding indexwise and subtract the subsequent element
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]
        max_sum = max(window_sum, max_sum)
    return max_sum

#Example
if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8,9,23,46,2,5,23,56,88,43]
    k = 5
    print(max_subarray_sum(nums,k))
