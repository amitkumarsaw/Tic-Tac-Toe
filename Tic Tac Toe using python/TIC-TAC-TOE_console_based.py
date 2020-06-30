# ============ TIC TAC TOE GAME ============

# CONTENTS :
  # 1. Game board
  # 2. a function to display the game board, display_board()
  # 3. A main function to call all the functions, play_game()
  # 4. A function to handle the turns, handle_turn()
  # 5. A function to flip between the players, flip_player()
  # 6. A function to check if the game ended or not, game_ended()
       # a> a function to check if it's a win, win()
               # -> function to check the columns, check_column()
               # => function to check the rows, check_row()
               # -> function to check the diagonals, check_diagonal()
       # b> a function to check if it's a tie, tie()



# Game Board, it's a list
board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

# global variable, set at true
game_still_going = True

# defining the function to display the game board(list) in the pattern of a tic-tac-toe game board
def display_board():
  print("\n")  
  print(board[0] + " | " + board[1] + " | " + board[2] + "         1   2   3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "         4   5   6")    
  print(board[6] + " | " + board[7] + " | " + board[8] + "         7   8   9")
  print("\n")


# Defining the main function which calls all the other functions  
def play_game():
  display_board()

  # looping to continue the game until a winner is found or a tie, in other words until game_still_going is true
  while game_still_going:
    print(current_player + "'s turn")
    handle_turn(current_player)
    game_ended()
    flip_player()

current_player = "x"


# Defining function to handle all the turns
def handle_turn(player):
  position = input("choose your position from 1-9 : ")    # taking input fron the player
  x = True
  # looping until the player gives a valid input
  while x:
    if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or board[int(position)-1] != "_":
      print("\n")
      position = input("INVALID POSITION. Enter another position from 1-9 : ")
      x = True
    else:  
      position = int(position) - 1   # converting the input into an integer
      board[position] = current_player    # to give the input to the game board
      display_board()     # display the board after input is added
      x = False   # it will stop the while loop


# Defining the function to check if the game ended or not, it will call the win() and tie() functions     
def game_ended():
  win()    # to check win condition
  tie()    # to check tie condition

# Defining the function to check a win, it will call the other 3 functions given under it
def win():
  check_column()
  check_row()
  check_diagonal()

# defining the function to check the column ( to check if a column has the same value or not )
def check_column():
  global game_still_going
  column1 = board[0] == board[1] == board[2] !="_"
  column2 = board[3] == board[4] == board[5] !="_"
  column3 = board[6] == board[7] == board[8] !="_"
  
  # if-elif statement to check the winning column and display the winner
  if column1:
    print("PLAYER " + board[0] + " WON THE GAME.")
  elif column2:
    print("PLAYER " + board[3] + " WON THE GAME.")
  elif column3:
    print("PLAYER " + board[6] + " WON THE GAME.")

  if column1 or column2 or column3:
    game_still_going = False  


# defining the function to check the rows ( to check if a row has the same value or not )    
def check_row():
  global game_still_going
  row1 = board[0] == board[3] == board[6] != "_"
  row2 = board[1] == board[4] == board[7] != "_"
  row3 = board[2] == board[5] == board[8] != "_"

  # if-elif statement to check the winning row and display the winner
  if row1:
    print("PLAYER " + board[0] + " WON THE GAME.")
  elif row2:
    print("PLAYER " + board[1] + " WON THE GAME.")
  elif row3:
    print("PLAYER " + board[2] + " WON THE GAME.")

  if row1 or row2 or row3:
    game_still_going = False    


# defining the function to check the diagonals ( to check if a diagonal has the same value or not )   
def check_diagonal():
  global game_still_going
  diagonal1 = board[0] == board[4] == board[8] != "_"
  diagonal2 = board[2] == board[4] == board[6] != "_"

  # if-elif statement to check the winning diagonal and display the winner
  if diagonal1:
    print("PLAYER " + board[0] + " WON THE GAME.")
  elif diagonal2:
    print("PLAYER " + board[2] + " WON THE GAME.")

  if diagonal1 or diagonal2:
    game_still_going = False

    
# defining the function to check a tie
def tie():
  global game_still_going
  if "_" not in board:
    print("it's a tie.")
    game_still_going = False
      

# defining a function to flip the players ( rotating the turns between the players )      
def flip_player():
  global current_player
  if current_player == "x":
    current_player = "o"
  elif current_player == "o":
    current_player = "x"

# calling the main function
play_game()
