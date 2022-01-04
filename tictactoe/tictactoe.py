"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countx = sum(x.count(X) for x in board)
    counto = sum(o.count(O) for o in board)
    if countx <= counto: #Since X always goes first in this implementation
        return X 
    else: 
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()
    for i in range(len(board)):
        for j in range((len(board[i]))):
            if board[i][j] == EMPTY:
                result.add((i,j))
    return result 



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    curr_player = player(board)
    if action not in actions(board): #space is not avaliable
        raise Exception("Invalid action - this space is not empty")
    else:
        #create deepcopy so original board is not alterated until move is actually chosen (in minimax)
        board_copy = copy.deepcopy(board) 
        board_copy[action[0]][action[1]] = curr_player
        return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check all rows
    for row in board:
        if EMPTY not in row and all(x == row[0] for x in row):
            return row[0]
    #check all columns
    for i in range(len(row)):
        col = [row[i] for row in board]
        if EMPTY not in row and all(x == col[0] for x in col):
            return col[0]
    #check first diagonal
    diagonal = [board[x][x] for x in range(len(board))]
    if EMPTY not in diagonal and all(x == diagonal[0] for x in diagonal):
        return diagonal[0]
    #check second diagonal
    diagonal = [board[x][2-x] for x in range(len(board))]
    if EMPTY not in diagonal and all(x == diagonal[0] for x in diagonal):
        return diagonal[0]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #empty space/s and no winner == not a terminal board
    if len(actions(board)) > 0 and winner(board) == None: 
        return False 
    else:
        return True 



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    Assumes given board is terminal
    """
    if winner(board) == X:
        return 1 
    elif winner(board) == O:
        return -1 
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None 
    if player(board) == X:
        return max_value(board)[1]
    else: 
        return min_value(board)[1]

# TODO - Refactor max_value and min_value    
def max_value(board):
    choices = []
    best_action = (None, None)
    if terminal(board):
        return (utility(board), best_action)
    best_v = -math.inf 
    for action in actions(board):
        curr_v = max(best_v, min_value(result(board, action))[0])
        if curr_v != best_v:
            best_v = curr_v
            best_action = action #TODO make choice random for equally valued moves
        if best_v == 1: #Pruning - found a winning move 
            break 
    return (best_v, best_action)

def min_value(board):
    best_action = (None, None)
    if terminal(board):
        return (utility(board), best_action)
    best_v = math.inf
    for action in actions(board):
        curr_v = min(best_v, max_value(result(board, action))[0])
        if curr_v != best_v:
            best_v = curr_v
            best_action = action #TODO make choice random for equally valued moves
        if best_v == -1: #Pruning - found a winning move
            break 
    return (best_v, best_action)