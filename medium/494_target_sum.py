# def findTargetSumWays(nums, target):
#     memo = {}

#     def dfs(i, cur_sum):
#         if i == len(nums):
#             if cur_sum == target:
#                 return 1
#             return 0

#         key = (i, cur_sum)

#         if key in memo:
#             return memo[key]

#         ways = dfs(i + 1, cur_sum + nums[i]) + dfs(i + 1, cur_sum - nums[i])

#         memo[key] = ways

#         return ways

#     return dfs(0, 0)


def findTargetSumWays(nums, target):
    dp = {0: 1}

    for num in nums:

        new_dp = {}

        for cur_sum, ways in dp.items():
            plus = cur_sum + num
            minus = cur_sum - num

            new_dp[plus] = new_dp.get(plus, 0) + ways
            new_dp[minus] = new_dp.get(minus, 0) + ways

        dp = new_dp

    return dp.get(target, 0)

tests = [
    ([1, 1, 1, 1, 1], 3, 5),
    ([1], 1, 1),

    ([1], -1, 1),
    ([1], 0, 0),

    ([0], 0, 2),
    ([0, 0], 0, 4),

    ([1, 2, 1], 0, 2),

    ([1, 2, 3], 0, 2),

    ([1, 2, 3], 2, 1),

    ([2, 2, 2], 2, 3),

    ([1, 1, 2, 3], 1, 3),

    ([0, 0, 0, 1], 1, 8),

    ([5, 10, 15], 10, 1),

    ([1, 2, 7, 9, 981], 1000000000, 0),
]


for nums, target, expected in tests:
    result = findTargetSumWays(nums, target)

    print(f"nums={nums}, target={target}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()