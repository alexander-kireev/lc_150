
def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    ans = 0

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        if target < nums[mid]:
            right = mid - 1
            ans = mid

        
        elif target > nums[mid]:
            left = mid + 1
            ans = mid + 1

    return ans








nums = [1,3,5,6]
target = 5


nums = [1,3,5,6]
target = 2
nums = [1,3,5,6]
target = 7


nums = [1,3,5,6]
target = 0

print(searchInsert(nums, target))