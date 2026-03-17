
def canJump(nums):
    last_index = len(nums) - 1
    furthest = nums[0]

    i = 0
    while i <= furthest:
        max_index = i + nums[i]

        if max_index > furthest:
            furthest = max_index
        
        if furthest >= last_index:
            return True

        i += 1
        
    return False








nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
nums = [0]
print(canJump(nums))