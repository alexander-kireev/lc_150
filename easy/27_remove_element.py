def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """

    k = 0

    cur = 0
    end = len(nums) - 1

    while cur <= end:

        while nums[cur] == val and end != cur:
            if nums[end] != val:
                nums[cur], nums[end] = nums[end], nums[cur]
            end -= 1
        
        if nums[cur] != val:
            k += 1
        
        cur += 1
        
    return k

val = 3
nums = []

print(removeElement(nums, val))

print(nums)