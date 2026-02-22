def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """


    

    
    cur = 0
    nxt = 1

    while nxt < len(nums):
        if nums[cur] < nums[nxt]:
            if cur != nxt - 1:
                nums[cur + 1] = nums[nxt]
            cur += 1

        nxt += 1 

    return cur + 1




nums = [0,0,1,1,1,2,2,3,3,4]


print(removeDuplicates(nums))
print(nums)