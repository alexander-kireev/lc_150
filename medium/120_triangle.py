def minimumTotal(triangle):
    dp = []
    for r in range(len(triangle)):
        dp.append([0] * (r + 1))

    dp[0][0] = triangle[0][0]

    for r in range(1, len(triangle)):
        for c in range(len(triangle[r])):
            if c == 0:
                dp[r][c] = dp[r - 1][c] + triangle[r][c]
            elif c == (len(triangle[r]) - 1):
                dp[r][c] = dp[r - 1][c - 1] + triangle[r][c]
            else:
                dp[r][c] = min(dp[r - 1][c - 1], dp[r - 1][c]) + triangle[r][c]

    return min(dp[-1])   



tests = [
    (
        [[2],
         [3, 4],
         [6, 5, 7],
         [4, 1, 8, 3]],
        11
    ),

    (
        [[-10]],
        -10
    ),

    (
        [[1],
         [2, 3]],
        3
    ),

    (
        [[1],
         [2, 3],
         [4, 5, 6]],
        7
    ),

    (
        [[-1],
         [2, 3],
         [1, -1, -3]],
        -1
    ),

    (
        [[5],
         [9, 1],
         [4, 7, 2],
         [8, 3, 6, 1]],
        9
    ),

    (
        [[0],
         [0, 0],
         [0, 0, 0]],
        0
    ),

    (
        [[2],
         [-3, 4],
         [6, -5, 7],
         [4, 1, -8, 3]],
        -5
    ),

    (
        [[1],
         [100, 2],
         [100, 100, 3],
         [100, 100, 100, 4]],
        10
    ),
]


for triangle, expected in tests:
    result = minimumTotal(triangle)

    print("triangle:")
    for row in triangle:
        print(row)

    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()