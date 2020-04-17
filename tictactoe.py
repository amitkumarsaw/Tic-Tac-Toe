board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

game_still_going = True

def display_board():
  print("\n")  
  print(board[0] + " | " + board[1] + " | " + board[2] + "         1   2   3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "         4   5   6")    
  print(board[6] + " | " + board[7] + " | " + board[8] + "         7   8   9")
  print("\n")


def play_game():
  display_board()

  while game_still_going:
    print(current_player + "'s turn")
    handle_turn(current_player)
    game_ended()
    flip_player()

current_player = "x"


def handle_turn(player):
  position = input("choose your position from 1-9 : ")
  x = True
  while x:
    if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or board[int(position)-1] != "_":
      print("\n")
      position = input("INVALID POSITION. Enter another position from 1-9 : ")
      x = True
    else:  
      position = int(position) - 1
      board[position] = current_player
      display_board()
      x = False


def game_ended():
  win()
  tie()


def win():
  check_column()
  check_raw()
  check_diagonal()


def check_column():
  global game_still_going
  column1 = board[0] == board[1] == board[2] !="_"
  column2 = board[3] == board[4] == board[5] !="_"
  column3 = board[6] == board[7] == board[8] !="_"
  
  if column1:
    print("PLAYER " + board[0] + " WON THE GAME.")
  elif column2:
    print("PLAYER " + board[3] + " WON THE GAME.")
  elif column3:
    print("PLAYER " + board[6] + " WON THE GAME.")

  if column1 or column2 or column3:
    game_still_going = False  


def check_raw():
  global game_still_going
  raw1 = board[0] == board[3] == board[6] != "_"
  raw2 = board[1] == board[4] == board[7] != "_"
  raw3 = board[2] == board[5] == board[8] != "_"

  if raw1:
    print("PLAYER " + board[0] + " WON THE GAME.")
  elif raw2:
    print("PLAYER " + board[1] + " WON THE GAME.")
  elif raw3:
    print("PLAYER " + board[2] + " WON THE GAME.")

  if raw1 or raw2 or raw3:
    game_still_going = False    


def check_diagonal():
  global game_still_going
  diagonal1 = board[0] == board[4] == board[8] != "_"
  diagonal2 = board[2] == board[4] == board[6] != "_"

  if diagonal1:
    print("PLAYER " + board[0] + " WON THE GAME.")
  elif diagonal2:
    print("PLAYER " + board[2] + " WON THE GAME.")

  if diagonal1 or diagonal2:
    game_still_going = False


def tie():
  global game_still_going
  if "_" not in board:
    print("it's a tie.")
    game_still_going = False
      

def flip_player():
  global current_player
  if current_player == "x":
    current_player = "o"
  elif current_player == "o":
    current_player = "x"


play_game()