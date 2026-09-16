def uniquePathsWithObstacles(obstacleGrid):
    grid = []
    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])

    for _ in range(rows):
        grid.append([0] * cols)

    for row in range(rows):
        for col in range(cols):
            if obstacleGrid[row][col] == 1:
                grid[row][col] = 0
            else:
                if row == 0 and col == 0:
                    grid[row][col] = 1
                elif row == 0:
                    grid[row][col] = grid[row][col - 1]
                elif col == 0:
                    grid[row][col] = grid[row - 1][col]
                else:
                    grid[row][col] = grid[row - 1][col] + grid[row][col - 1]

    return grid[-1][-1]


tests = [
    (
        [[0,0,0],
         [0,1,0],
         [0,0,0]],
        2
    ),

    (
        [[0,1],
         [0,0]],
        1
    ),

    ([[0]], 1),
    ([[1]], 0),

    ([[0,0]], 1),

    (
        [[0],
         [0]],
        1
    ),

    ([[0,1,0]], 0),

    (
        [[0],
         [1],
         [0]],
        0
    ),

    (
        [[0,0],
         [0,0]],
        2
    ),

    (
        [[0,0,0],
         [0,0,0],
         [0,0,0]],
        6
    ),

    (
        [[0,0,0],
         [1,1,0],
         [0,0,0]],
        1
    ),

    (
        [[0,0,0],
         [0,0,0],
         [0,1,0]],
        3
    ),

    (
        [[0,0,1],
         [0,0,0],
         [0,0,0]],
        5
    ),
]


for obstacleGrid, expected in tests:
    result = uniquePathsWithObstacles(obstacleGrid)

    print("grid:")
    for row in obstacleGrid:
        print(row)

    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()