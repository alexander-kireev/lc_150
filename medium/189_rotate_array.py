def rotate(nums, k):
    k = k % len(nums)
    def rotate_helper(left, right):
        for i in range((right - left) // 2):
            nums[left + i], nums[right - i - 1] = nums[right - i - 1], nums[left + i]
    
    rotate_helper(0, len(nums))
    rotate_helper(0, k)
    rotate_helper(k, len(nums))




nums = [1,2,3,4,5,6,7]
k = 3
# Output: [5,6,7,1,2,3,4]
rotate(nums, k)