def game_of_life(board):
    rows = len(board)
    cols = len(board[0])
    board2 = [ [0] * cols for _ in range(rows)]

    def live_neighbours(r, c):
        live = 0

        start_r = r - 1
        start_c = c - 1

        for x in range(start_r, start_r + 3):
            for y in range(start_c, start_c + 3):
                neighbour_r = x
                neighbour_c = y

                if neighbour_r == r and neighbour_c == c:
                    pass
                elif 0 <= neighbour_r < rows and 0 <= neighbour_c < cols:
                    if board[neighbour_r][neighbour_c] == 1:
                        live += 1
        
        return live

    for r in range(rows):
        for c in range(cols):
            state = board[r][c]
            next_state = 0
            live = live_neighbours(r, c)
        
            if state == 1:
                if 2 <= live <= 3:
                    next_state = 1
            elif state == 0:
                if live == 3:
                    next_state = 1
            
            board2[r][c] = next_state

    for r in range(rows):
        for c in range(cols):
            board[r][c] = board2[r][c]









def run_test(board):
    game_of_life(board)
    print(board)


run_test([[0,1,0],
          [0,0,1],
          [1,1,1],
          [0,0,0]])
# [[0,0,0],
#  [1,0,1],
#  [0,1,1],
#  [0,1,0]]


run_test([[1,1],
          [1,0]])
# [[1,1],
#  [1,1]]


run_test([[0]])
# [[0]]


run_test([[1]])
# [[0]]
# single live cell dies from under-population


run_test([[1,1,1]])
# [[0,1,0]]


run_test([[1],
          [1],
          [1]])
# [[0],
#  [1],
#  [0]]


run_test([[0,0,0],
          [0,1,0],
          [0,0,0]])
# [[0,0,0],
#  [0,0,0],
#  [0,0,0]]


run_test([[1,1,0],
          [1,1,0],
          [0,0,0]])
# [[1,1,0],
#  [1,1,0],
#  [0,0,0]]
# stable 2x2 block


run_test([[0,1,0],
          [0,1,0],
          [0,1,0]])
# [[0,0,0],
#  [1,1,1],
#  [0,0,0]]
# blinker pattern