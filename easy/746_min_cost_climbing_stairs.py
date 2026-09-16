def minCostClimbingStairs(cost):

    memo = {
        0: 0,
        1: cost[0],
        2: cost[1],
    }

    def top_down(n):

        if n in memo:
            return memo[n]

        memo[n] = min(top_down(n - 1), top_down(n - 2)) + cost[n - 1]
        return memo[n]

    top_down(len(cost))
    return min(memo[len(cost)], memo[len(cost) - 1])


# def minCostClimbingStairs(cost):
#     prev_prev = cost[0]
#     prev = cost[1]

#     for i in range(2, len(cost)):
#         cur = min(prev, prev_prev) + cost[i]
#         prev_prev = prev
#         prev = cur

#     return min(prev, prev_prev)

tests = [
    ([10, 15, 20], 15),

    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),

    ([0, 0], 0),
    ([1, 1], 1),

    ([5, 10, 15], 10),

    ([10, 15, 20, 5], 20),

    ([1, 2, 3, 4], 6),

    ([10, 1, 10, 1, 10, 1], 3),

    ([2, 2, 2, 2, 2], 4),

    ([0, 1, 0, 1, 0, 1], 0),

    ([100, 1, 1, 100, 1, 1, 100], 4),

    ([3, 4, 5, 1, 2, 3], 8),
]


for cost, expected in tests:
    result = minCostClimbingStairs(cost)

    print(f"cost={cost}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()