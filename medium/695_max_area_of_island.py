def maxAreaOfIsland(grid):
    rows = len(grid)
    cols = len(grid[0])

    max_island = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                island = 0
                cells = [[row, col]]
                grid[row][col] = 0

                while cells:
                    r, c = cells.pop()
                    island += 1

                    candidates = [
                        [r - 1, c],
                        [r, c + 1],
                        [r + 1, c],
                        [r, c - 1],
                    ]

                    for rc, cc in candidates:

                        if -1 < rc < rows and -1 < cc < cols and grid[rc][cc] == 1:
                            cells.append([rc, cc])
                            grid[rc][cc] = 0

                max_island = max(max_island, island)

    return max_island

tests = [
    (
        [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0],
        ],
        6
    ),

    (
        [[0,0,0,0,0,0,0,0]],
        0
    ),

    (
        [[1]],
        1
    ),

    (
        [[0]],
        0
    ),

    (
        [
            [1,1],
            [1,1],
        ],
        4
    ),

    (
        [
            [1,0,1],
            [0,1,0],
            [1,0,1],
        ],
        1
    ),

    (
        [
            [1,1,0,0],
            [1,0,0,1],
            [0,0,1,1],
            [1,0,1,1],
        ],
        5
    ),

    (
        [
            [1,1,1,0,1],
            [0,1,0,0,1],
            [0,1,1,1,0],
        ],
        7
    ),

    (
        [
            [0,1,0],
            [1,1,1],
            [0,1,0],
        ],
        5
    ),
]


for grid, expected in tests:
    test_grid = [row[:] for row in grid]

    result = maxAreaOfIsland(test_grid)

    print("grid:")
    for row in grid:
        print(row)

    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()