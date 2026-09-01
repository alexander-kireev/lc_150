def rob(nums):
        
    n = len(nums)
    if n == 1:
        return nums[0]

    dp = [nums[0], max(nums[0], nums[1])]
    best = max(dp[0], dp[1])

    for i in range(2, n):
        dp.append(max(dp[i - 1], dp[i - 2] + nums[i]))
        best = max(best, dp[i])
    
    return best


tests = [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([1], 1),
    ([0], 0),
    ([2, 1], 2),
    ([1, 2], 2),
    ([2, 1, 1, 2], 4),
    ([5, 1, 1, 5], 10),
    ([2, 7, 9, 3, 1, 8], 18),
    ([10, 1, 1, 10, 1, 1, 10], 30),
    ([4, 4, 4, 4], 8),
    ([0, 0, 0, 0], 0),
]

for nums, expected in tests:
    result = rob(nums)

    print(
        f"nums={nums} -> {result} "
        f"(expected {expected})"
    )