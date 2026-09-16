def maxSumAfterPartitioning(arr, k):
    dp = arr.copy()

    for i in range(1, len(arr)):

        if i >= k:
            j = (i - k) + 1
        else:
            j = 0

        while j <= i:

            max_num = max(arr[j:i + 1])

            diff = (i - j) + 1
            can_get = max_num * diff

            best_before = 0
            if j != 0:
                best_before = dp[j - 1]

            dp[i] = max(dp[i], can_get + best_before)
            j += 1

    return dp[-1]


tests = [
    ([1, 15, 7, 9, 2, 5, 10], 3, 84),
    ([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4, 83),
    ([1], 1, 1),

    ([1, 2, 3], 1, 6),
    ([1, 2, 3], 2, 7),
    ([1, 2, 3], 3, 9),

    ([5, 5, 5], 2, 15),
    ([10, 1, 1, 10], 2, 40),

    ([2, 1, 4, 5, 1, 3, 3], 3, 30),

    ([0, 0, 0], 2, 0),

    ([1, 100, 1, 1], 2, 202),
]


for arr, k, expected in tests:
    result = maxSumAfterPartitioning(arr, k)

    print(f"arr={arr}, k={k}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()