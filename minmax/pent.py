import numpy as np
import ast

BOARD = np.zeros((6, 6), dtype=np.int32)
print(BOARD)

def rotate_subsquare(BOARD, subsquare_index, direction):
    # Define the subsquares
    subsquares = [
        BOARD[:3, :3],
        BOARD[:3, 3:],
        BOARD[3:, :3],
        BOARD[3:, 3:]
    ]

    # Rotate the specified subsquare
    if direction == 1:
        subsquares[subsquare_index - 1] = np.rot90(subsquares[subsquare_index - 1], -1)
    elif direction == -1:
        subsquares[subsquare_index - 1] = np.rot90(subsquares[subsquare_index - 1], 1)

    # Reconstruct the 6x6 array
    BOARD[:3, :3] = subsquares[0]
    BOARD[:3, 3:] = subsquares[1]
    BOARD[3:, :3] = subsquares[2]
    BOARD[3:, 3:] = subsquares[3]

    return BOARD

def is_winning(board, player):
    for i in range(6):
        for j in range(2):
            if np.all(board[i, j:j+5] == player) or np.all(board[j:j+5, i] == player):
                return True
    for i in range(2):
        for j in range(2):
            if np.all(np.diag(board[i:i+5, j:j+5]) == player) or np.all(np.diag(np.fliplr(board[i:i+5, j:j+5])) == player):
                return True
    return False

def is_full(board):
    return not np.any(board == 0)

def evaluate_board(board):
    if is_winning(board, 1):
        return 1
    elif is_winning(board, 2):
        return -1
    else:
        return 0

def minimax(board, depth, alpha, beta, maximizingPlayer):
    score = evaluate_board(board)
    if depth == 0 or score == 1 or score == -1 or is_full(board):
        return score

    if maximizingPlayer:
        maxEval = float('-inf')
        for i in range(6):
            for j in range(6):
                if board[i][j] == 0:
                    board[i][j] = 1
                    eval = minimax(board, depth - 1, alpha, beta, False)
                    board[i][j] = 0
                    maxEval = max(maxEval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return maxEval
    else:
        minEval = float('inf')
        for i in range(6):
            for j in range(6):
                if board[i][j] == 0:
                    board[i][j] = 2
                    eval = minimax(board, depth - 1, alpha, beta, True)
                    board[i][j] = 0
                    minEval = min(minEval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return minEval

def best_move(board):
    bestVal = float('-inf')
    bestMove = None
    for i in range(6):
        for j in range(6):
            if board[i][j] == 0:
                board[i][j] = 1
                moveVal = minimax(board, 3, float('-inf'), float('inf'), False)  # Reduce depth to 3
                board[i][j] = 0
                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal
    return bestMove

def get_move(board):
    move = input('Enter move (row, col): ')
    try:
        move_tuple = ast.literal_eval(move)
        if board[move_tuple[0], move_tuple[1]] == 0:
            board[move_tuple[0], move_tuple[1]] = 1
            print(board)
            sub_index = int(input('Enter the subsquare to rotate (1-4): '))
            direction = int(input('Enter the direction (-1, 0, 1): '))
            board = rotate_subsquare(board, sub_index, direction)
            print(board)
        else:
            print("Invalid move! Try again.")
            get_move(board)
    except Exception as e:
        print(f"Exception '{str(e)}' occurred. Try again.")
        get_move(board)

def random_move(board):
    empty_cells = [(i, j) for i in range(6) for j in range(6) if board[i][j] == 0]
    length = len(empty_cells)
    rand = np.random.randint(0, length)
    return empty_cells[rand]

def play_game(BOARD):
    turn_count = 0
    while True:
        # Player move
        get_move(BOARD)
        turn_count += 1
        if is_winning(BOARD, 1):
            print("Player wins!")
            break
        if is_full(BOARD):
            print("It's a draw!")
            break
        
        # Computer move
        if turn_count <= 3:
            move = random_move(BOARD)
        else:
            move = best_move(BOARD)
        
        if move:
            BOARD[move[0]][move[1]] = 2
            print("Computer moved:")
            print(BOARD)
            sub_index = np.random.randint(1, 5)
            direction = np.random.choice([-1, 1, 0])
            BOARD = rotate_subsquare(BOARD, sub_index, direction)
            print("Computer rotated:")
            print(BOARD)
            if is_winning(BOARD, 2):
                print("Computer wins!")
                break
            if is_full(BOARD):
                print("It's a draw!")
                break

play_game(BOARD)
