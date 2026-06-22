def unique_paths(m, n):
    grid = []

    for row in range(m):
        grid.append([])
        for col in range(n):
            if row == 0 or col == 0:
                grid[row].append(1)
            else:
                grid[row].append(0)
    
    for row in range(1, m):
        for col in range(1, n):
            grid[row][col] = grid[row - 1][col] + grid[row][col - 1]


    return grid[m - 1][n - 1]


assert unique_paths(3, 7) == 28
assert unique_paths(3, 2) == 3
assert unique_paths(1, 1) == 1
assert unique_paths(1, 5) == 1
assert unique_paths(5, 1) == 1
assert unique_paths(2, 2) == 2
assert unique_paths(3, 3) == 6
assert unique_paths(4, 4) == 20