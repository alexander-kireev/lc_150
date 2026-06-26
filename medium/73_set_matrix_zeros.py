def set_zeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    zero_rows = set()
    zero_cols = set()

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)

    for r in range(rows):
        for c in range(cols):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0
    



def run_test(matrix):
    set_zeroes(matrix)
    print(matrix)


run_test([[1,1,1],
          [1,0,1],
          [1,1,1]])
# [[1,0,1],
#  [0,0,0],
#  [1,0,1]]


run_test([[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]])
# [[0,0,0,0],
#  [0,4,5,0],
#  [0,3,1,0]]


run_test([[1]])
# [[1]]


run_test([[0]])
# [[0]]


run_test([[1,2,3]])
# [[1,2,3]]


run_test([[1,0,3]])
# [[0,0,0]]


run_test([[1],
          [0],
          [3]])
# [[0],
#  [0],
#  [0]]


run_test([[1,2,3],
          [4,5,6],
          [7,8,9]])
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]


run_test([[1,2,0],
          [4,5,6],
          [0,8,9]])
# [[0,0,0],
#  [0,5,0],
#  [0,0,0]]