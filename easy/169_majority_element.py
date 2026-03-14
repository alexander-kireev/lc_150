import math
def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    found = {}
    target = len(nums)//2
    print(target)
    for num in nums:
        if num in found:
            found[num] += 1
        else:
            found[num] = 1

        if found[num] > target:
            return num

    
nums = [2,2,1,1,1,2,2]





def majorityElement_canon(nums):

    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        
        if num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate


print(majorityElement_canon(nums))