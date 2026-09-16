def solve(board):
    rows = len(board)
    cols = len(board[0])

    safe = set()
    visited = set()

    for r in range(rows):
        for c in range(cols):
            if 0 < r < rows - 1 and 0 < c < cols - 1:
                continue

            if board[r][c] == "O":
                safe.add((r, c))

    new_safe = set()

    for s in safe:
        new_safe.add(s)
        if s in visited:
            continue

        to_explore = [s]

        while to_explore:
            cell = to_explore.pop()
            visited.add(cell)

            r, c = cell

            candidates = [
                [r - 1, c],
                [r, c + 1],
                [r + 1, c],
                [r, c - 1]
            ]

            for row, col in candidates:
                if (row, col) in visited or (row, col) in to_explore:
                    continue

                if -1 < row < rows and -1 < col < cols and board[row][col] == "O":
                    to_explore.append((row, col))
                    new_safe.add((row, col))

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if board[r][c] == "O" and (r, c) not in new_safe:
                board[r][c] = "X"
    


tests = [
    (
        [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]
        ],
        [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","O","X","X"]
        ]
    ),

    (
        [["X"]],
        [["X"]]
    ),

    (
        [["O"]],
        [["O"]]
    ),

    (
        [
            ["O","O"],
            ["O","O"]
        ],
        [
            ["O","O"],
            ["O","O"]
        ]
    ),

    (
        [
            ["X","X","X"],
            ["X","O","X"],
            ["X","X","X"]
        ],
        [
            ["X","X","X"],
            ["X","X","X"],
            ["X","X","X"]
        ]
    ),

    (
        [
            ["O","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","X","X","X"]
        ],
        [
            ["O","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"]
        ]
    ),

    (
        [
            ["X","O","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","X","X","X"]
        ],
        [
            ["X","O","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","X","X","X"]
        ]
    ),

    (
        [
            ["X","X","X","X","X"],
            ["X","O","O","O","X"],
            ["X","O","X","O","X"],
            ["X","O","O","O","X"],
            ["X","X","X","X","X"]
        ],
        [
            ["X","X","X","X","X"],
            ["X","X","X","X","X"],
            ["X","X","X","X","X"],
            ["X","X","X","X","X"],
            ["X","X","X","X","X"]
        ]
    ),

    (
        [
            ["X","X","O","X","X"],
            ["X","O","O","O","X"],
            ["X","X","O","X","X"],
            ["X","X","X","X","X"]
        ],
        [
            ["X","X","O","X","X"],
            ["X","O","O","O","X"],
            ["X","X","O","X","X"],
            ["X","X","X","X","X"]
        ]
    ),
]


for board, expected in tests:
    test_board = [row[:] for row in board]

    result = solve(test_board)

    print("input:")
    for row in board:
        print(row)

    print("result:")
    for row in test_board:
        print(row)

    print("expected:")
    for row in expected:
        print(row)

    print("correct:", test_board == expected)
    print("returned:", result)
    print()