from math import inf

def minPathSum(grid):

    dp = []
    m = len(grid)
    n = (len(grid[0]))

    for _ in range(m):
        dp.append([inf] * n)

    dp[0][0] = grid[0][0]

    for c in range(1, n):
        dp[0][c] = dp[0][c - 1] + grid[0][c]

    for r in range(1, m):
        dp[r][0] = dp[r - 1][0] + grid[r][0]

    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = min(dp[r][c - 1], dp[r - 1][c]) + grid[r][c]

    return dp[-1][-1]




















tests = [
    (
        [[1, 3, 1],
         [1, 5, 1],
         [4, 2, 1]],
        7
    ),

    (
        [[1, 2, 3],
         [4, 5, 6]],
        12
    ),

    (
        [[5]],
        5
    ),

    (
        [[1, 2, 3, 4]],
        10
    ),

    (
        [[1],
         [2],
         [3],
         [4]],
        10
    ),

    (
        [[0, 0],
         [0, 0]],
        0
    ),

    (
        [[1, 100, 100],
         [1,   1, 100],
         [100, 1,   1]],
        5
    ),

    (
        [[5, 1, 1],
         [9, 9, 1],
         [9, 9, 1]],
        9
    ),

    (
        [[1, 2, 5],
         [3, 2, 1]],
        6
    ),

    (
        [[1, 9, 1, 1],
         [1, 1, 1, 9],
         [9, 9, 1, 1]],
        6
    ),
]


for grid, expected in tests:
    result = minPathSum(grid)

    print("grid:")
    for row in grid:
        print(row)

    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()