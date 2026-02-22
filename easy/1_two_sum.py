def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    seen = {}

    for i in range(len(nums)):
        needed = target - nums[i]

        if needed in seen:
            return [i, seen[needed]]
        
        seen[nums[i]] = i

    return []
    