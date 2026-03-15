def removeDuplicates(nums) -> int:
    
    return_length = len(nums)
    last_int = nums[0]
    count_last_int = 1
    
    for i in range(1,len(nums)):
        if nums[i] == last_int:
            count_last_int += 1
        else:
            last_int = nums[i]
            count_last_int = 1

        if count_last_int > 2:
            return_length -= 1
            nums[i] = '_'
    
    for i in range(len(nums)):
        if nums[i] == '_':
            j = i + 1

            while j < len(nums) and nums[j] == '_':
                j += 1

            if j >= len(nums):
                return return_length
            
            nums[i], nums[j] = nums[j], nums[i]

    return return_length
    

nums = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(nums))

# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements 
# of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).