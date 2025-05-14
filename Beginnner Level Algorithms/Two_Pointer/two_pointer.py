def two_sum_sorted(nums, target):
    if len(nums) < 2:
        return False

    left, right = 0 , len(nums)-1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -=1
    return False

#usage
if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8]
    target = 9 # [[1, 8], [2, 7], [3, 6], [4, 5]]
    print(two_sum_sorted(nums, target))

