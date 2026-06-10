

def islands(grid):
    islands = 0
    rows = len(grid)
    cols = len(grid[0])

    # helper search function
    def search(r, c):

        # ensure grid[r][c] is valid and land
        if not (0 <= r < rows and
                0 <= c < cols and
                grid[r][c] == "1"):
                    return
        
        # update to water
        grid[r][c] = "0"

        # get neighbours
        neighbours = [
            (r - 1, c),
            (r, c + 1),
            (r + 1, c),
            (r, c - 1)
        ]

        # search from each neighbour
        for row, col in neighbours:
             search(row, col)

    # search each row, column
    for r in range(rows):
        for c in range(cols):
            
            # if land, means start of island
            if grid[r][c] == "1":
                islands += 1

                # search neighbours
                search(r, c)
                    
    return islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


# grid = [
#   ["x","x","0","0","0"],
#   ["x","x","0","0","0"],
#   ["0","0","x","0","0"],
#   ["0","0","0","x","1"]
# ]

#Output: 3
print(islands(grid))