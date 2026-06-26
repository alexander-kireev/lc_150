def spiral_order(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    length = rows * cols
    output = []
    visited = set()

    row = 0
    col = 0
    dir = 0

    while len(visited) < length:
        visited.add((row, col))
        output.append(matrix[row][col])

        if dir == 0:
            if (col + 1 < cols) and ((row, col + 1) not in visited):
                col += 1
            else:
                dir = 1
                row += 1
        elif dir == 1:
            if (row + 1 < rows) and ((row + 1, col) not in visited):
                row += 1
            else:
                dir = 2
                col -= 1
        elif dir == 2:
            if (col - 1 > -1) and ((row, col - 1) not in visited):
                col -= 1
            else:
                dir = 3
                row -= 1
        elif dir == 3:
            if (row - 1 > -1) and ((row - 1, col) not in visited):
                row -= 1
            else:
                dir = 0
                col += 1

    return output






print(spiral_order([[1,2,3],[4,5,6],[7,8,9]]))
# [1,2,3,6,9,8,7,4,5]

print(spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
# [1,2,3,4,8,12,11,10,9,5,6,7]

print(spiral_order([[1]]))
# [1]

print(spiral_order([[1,2,3,4]]))
# [1,2,3,4]

print(spiral_order([[1],[2],[3],[4]]))
# [1,2,3,4]

print(spiral_order([[1,2],[3,4]]))
# [1,2,4,3]

print(spiral_order([[1,2,3],[4,5,6]]))
# [1,2,3,6,5,4]

print(spiral_order([[1,2],[3,4],[5,6]]))
# [1,2,4,6,5,3]

print(spiral_order([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,16]
]))
# [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]