#Jared McMahon "JJ McBeans"
#12/10/18
#tickity tackity toeity

#global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

#functions
def display_instructions():
    print("""Welcome to TIC TAC TOE
          In in TIC TAC TOE you will be competing against a computer to get
          three in a row


              0 | 1 | 2
              ---------
              3 | 4 | 5
              ---------
              6 | 7 | 8

              """)

#########################################################################################################

def ask_yes_no(question):
    """Ask a yes or no question"""
    response = None
    while response not in ("y","n"):
          response = input(question).lower()
    return response

#########################################################################################################

def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low, high):
                break
            else:
                response = input(question)
        else:
            print("you must enter a number")
            response = input(question)
    return int(response)

#########################################################################################################
def pieces():
    go_first = ask_yes_no("do you want to go first y or n")
    if go_first == "y":
        print("Ha, you will lose either way")
        player_piece = X
        computer_piece = O
    else:
        print("Ha, you will lose either way")
        player_piece = O
        computer_piece = X
    return player_piece, computer_piece

#########################################################################################################

def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

#########################################################################################################

def display_board():
    """display game on screen"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8])

#########################################################################################################

def legal_moves():
    moves = []
    for square in range(NUM_SQUARES):
        if moves == "":
            moves.append(square)
        else:
            continue
        return moves

#########################################################################################################

def winner(board):
    """determine the game winner"""
    WAYS_TO_WIN = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (0,4,8),
                   (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE

    return None







    
