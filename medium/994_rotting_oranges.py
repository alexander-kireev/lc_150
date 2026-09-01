from collections import deque

def orangesRotting(grid):

    minutes = 0

    fresh = 0
    rotten = deque()

    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1
            elif grid[r][c] == 2:
                rotten.append((r, c))


    while rotten and fresh > 0:
        minutes += 1


        for _ in range(len(rotten)):
            r, c = rotten.popleft()

            candidates = [
                (r - 1, c),
                (r, c + 1),
                (r + 1, c),
                (r, c - 1)
            ]

            for candidate in candidates:

                row = candidate[0]
                col = candidate[1]

                if -1 < row < rows and -1 < col < cols and grid[row][col] == 1:
                    fresh -= 1
                    grid[row][col] = 2
                    rotten.append((row, col))

    if fresh > 0:
        return -1

    return minutes


tests = [
    (
        [[2, 1, 1],
         [1, 1, 0],
         [0, 1, 1]],
        4
    ),

    (
        [[2, 1, 1],
         [0, 1, 1],
         [1, 0, 1]],
        -1
    ),

    (
        [[0, 2]],
        0
    ),

    (
        [[0]],
        0
    ),

    (
        [[1]],
        -1
    ),

    (
        [[2]],
        0
    ),

    (
        [[2, 1]],
        1
    ),

    (
        [[2, 1, 1, 1]],
        3
    ),

    (
        [[2, 1],
         [1, 1]],
        2
    ),

    (
        [[2, 2],
         [2, 1]],
        1
    ),

    (
        [[2, 1, 0],
         [1, 0, 1],
         [0, 1, 1]],
        -1
    ),

    (
        [[2, 1, 1],
         [1, 1, 1],
         [1, 1, 2]],
        2
    ),

    (
        [[0, 0, 0],
         [0, 0, 0]],
        0
    ),
]


for grid, expected in tests:
    test_grid = [row[:] for row in grid]

    result = orangesRotting(test_grid)

    print("grid:")
    for row in grid:
        print(row)

    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()