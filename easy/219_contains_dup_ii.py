def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """

    seen = {}

    for i in range(len(nums)):
        if nums[i] in seen:
            if abs(seen[nums[i]] - i) <= k:
                return True
        seen[nums[i]] = i
    return False
        