from math import inf
def minFallingPathSum(matrix):
    grid = matrix.copy()

    for r in range(1, len(matrix)):
        for c in range(len(matrix[0])):

            if c == 0:
                left = inf
            else:
                left = matrix[r - 1][c - 1]

            mid = matrix[r - 1][c]

            if c == len(matrix[0]) - 1:
                right = inf
            else:
                right = matrix[r - 1][c + 1]

            existing = matrix[r][c]
            
            grid[r][c] = min(left, mid, right) + existing

    return min(grid[-1])

tests = [
    # (
    #     [[2, 1, 3],
    #      [6, 5, 4],
    #      [7, 8, 9]],
    #     13
    # ),

    # (
    #     [[-19, 57],
    #      [-40, -5]],
    #     -59
    # ),

    # (
    #     [[5]],
    #     5
    # ),

    # (
    #     [[1, 2],
    #      [3, 4]],
    #     4
    # ),

    # (
    #     [[1, 100, 1],
    #      [100, 1, 100],
    #      [1, 100, 1]],
    #     3
    # ),

    # (
    #     [[10, 2, 3],
    #      [4, 50, 6],
    #      [7, 8, 9]],
    #     13
    # ),

    # (
    #     [[-1, 2, 3],
    #      [4, -5, 6],
    #      [7, 8, -9]],
    #     -15
    # ),

    # (
    #     [[100, 100, 1],
    #      [100, 1, 100],
    #      [1, 100, 100]],
    #     3
    # ),

    # (
    #     [[0, 0, 0],
    #      [0, 0, 0],
    #      [0, 0, 0]],
    #     0
    # ),

    (
        [[3, 1, 2, 8],
         [4, 9, 1, 7],
         [6, 2, 5, 3],
         [8, 4, 1, 9]],
        7
    ),
]


for matrix, expected in tests:
    result = minFallingPathSum(matrix)

    print("matrix:")
    for row in matrix:
        print(row)

    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()