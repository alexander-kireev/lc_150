def rob(nums):
    if len(nums) < 2:
        return nums[0]

    prev1 = nums[0]
    prev2 = 0

    for i in range(1, len(nums)):
        cur = max(nums[i] + prev2, prev1)
        prev2 = prev1
        prev1 = cur

    return prev1

nums = [2,7,9,3,1]
#Output: 12

print(rob(nums))