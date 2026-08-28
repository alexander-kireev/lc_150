def lengthOfLIS(nums):
    best = 0
    dp = [1] * len(nums)
    dp[-1] = 1
    
    cur = len(nums) - 2
    while cur >= 0:
        prev = cur + 1

        while prev < len(nums):
            if nums[cur] < nums[prev]:
                dp[cur] = max(dp[cur], dp[prev] + 1)
            elif nums[cur] == nums[prev]:
                dp[cur] = max(dp[cur], dp[prev])
                break
            prev += 1
        
        # if prev == len(nums):
        #     dp[cur] = 1
        # else:
        #     if nums[cur] == nums[prev]:
        #         dp[cur] = dp[prev]
        #     else:
        #         dp[cur] = dp[prev] + 1

        best = max(dp[cur], best)
        cur -= 1

    return best

tests = [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1),
    ([1], 1),
    ([1, 2, 3, 4, 5], 5),
    ([5, 4, 3, 2, 1], 1),
    ([3, 1, 2], 2),
    ([4, 10, 4, 3, 8, 9], 3),
    ([2, 2, 2, 3], 2),
    ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
    ([-3, -2, -1, 0], 4),
    ([2, 5, 1, 8, 3, 9, 4], 4),
]

for nums, expected in tests:
    result = lengthOfLIS(nums)

    print(
        f"nums={nums} -> {result} "
        f"(expected {expected})"
    )