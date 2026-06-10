

def find_min(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

# nums = [4,5,6,7,8,9,0,1,2]
# nums = [8,0,1,2,3,4,5,6,7]
# nums = [6,7,8,9,0,1,2,3,4]
# nums = [3,2,1] # done
nums = [1,2,3] # done
nums = [1,2]
nums = [2,1]
print(find_min(nums))