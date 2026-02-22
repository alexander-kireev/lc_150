def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if not nums:
        return 0

    longest = 1
    seen = set(nums)

    for num in seen:
        temp = 1

        if (num - 1) not in seen:
    
            while (num + 1) in seen:
                temp += 1
                num += 1
        
        if temp > longest:
            longest = temp
    
    return longest
        