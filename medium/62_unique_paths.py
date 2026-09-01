def uniquePaths(m, n):
    dp = []
    
    for _ in range(m):
        row = [1] * n
        dp.append(row)

    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
    
    return dp[m - 1][n - 1]





tests = [
    (3, 7, 28),
    (3, 2, 3),
    (1, 1, 1),
    (1, 5, 1),
    (5, 1, 1),
    (2, 2, 2),
    (2, 3, 3),
    (3, 3, 6),
    (4, 4, 20),
    (5, 5, 70),
    (3, 10, 45),
    (10, 3, 45),
]

for m, n, expected in tests:
    result = uniquePaths(m, n)

    print(
        f"m={m}, n={n} -> {result} "
        f"(expected {expected})"
    )