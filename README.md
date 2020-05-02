> # INTRODUCTION : 

## `MAKING Tic-Tac-Toe GAME USING PYTHON :`
Under this project i'm making :  
* Console based Tic-Tac-Toe game  
* Tic-Tac-Toe  with a GUI ( Desktop application ) 
* Tic-Tac-Toe web application  

## `WHAT IS Tic-Tac-Toe GAME :`    
Tic-Tac-Toe is a simple game played with 'X' and 'O'. the is made up of 3 rows and 3 columns :  

` X | O | X`  
--
` O | X | X `  
` X | O | O `  

`Here 2nd diagonal has same values i.e. "x". Therefore "X" is the winner. Similarly if a row or a column has a same value then that row or column is the winner.`  

## `WHICH EDITOR TO USE  :`

Personally i'm using "VSCode" but u can also use ,  
   * Spyder
   * PyCharm
   * Atom
   * Sublime Text 3  
   and many more.  
---  
---

> # CONSOLE BASED Tic-Tac-Toe GAME :

# [COMPLETE CODE link](https://github.com/AMIT-ZING/Tic-Tac-Toe/blob/master/tictactoe.py)

# STRUCTURE :

The program starts from a list of 9 members as we need 9 spaces in our tictactoe game.  
Now these spaces needs to appear like tictactoe game board , for that we use the code below :  
```python
        def display_board():
            print("\n")  
            print(board[0] + " | " + board[1] + " | " + board[2])
            print(board[3] + " | " + board[4] + " | " + board[5])    
            print(board[6] + " | " + board[7] + " | " + board[8])
            print("\n")  
 ```    

"\n" codes for spaces above and below the game board.
 
Now we will make a main fn which will trigger all the steps involved in the game , we will name it "play_game" .

`This main fn involves game steps like :`  
1. Displaying the board , dispaly_board  
1. A while loop with a global variable which is set to True , game_still_going
      
The while loop contains further steps or functions which needs to be repeated until the game is running(game_still_going = true).  

`The functions are :`  
1. Handling the turn of players , handle_turn()
1. Checking if the game ended or not , game_ended()
1. Flipping between the two players , flip_player()  

the while loop will also contain the print statement to show whose turn it is.

We will give a variable "current_player" and assign it an initial value "x" .  
`Now we will define the handle_turn() fn :`
         
1. Take the input from the user and assign it to the "position" variable,  
```python                   
        position = input("choose your position from 1-9 : ")
```                   
2. Place any variable and give it a True value ,  
```python
        x = True  
```
3. Place a while loop for x = True to continue the process until we get a valid input from the user , 
```python 
        while x:
```                         
4. Give an "if" statement under the "while" statement under the condition that the values of "position" comes under 1 to 9 and there must be an empty place for that input .  
If the condition under "if" is true then the user is again asked for another valid input and the process is repeated again .  
If the new input is valid then the "else" statement works which will simply convert the input into integer and place it in the game board .

`The while statement will then be stopped by giving x = False ,`  
```python
        if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or board[int(position)-1] != "_":
            print("\n")
            position = input("INVALID POSITION. Enter another position from 1-9 : ")
            x = True
        else:  
            position = int(position) - 1
            board[position] = current_player
            display_board()
            x = False
```

`Now we will define the "game_ended()" fn :`  
This will just contain the another two functions, 
1. win()
2. tie()

`Defining the "win()" fn :`  
It will just contain 3 other functions ,
1. check_column()
2. check_raw()
3. check_diagonals()

`Defining check_column() fn ,`   
It will compare the 3 columns one by one for a common value "x" or "o" and assign it to 3 variables.  
```python
        column1 = board[0] == board[1] == board[2] !="_"
        column2 = board[3] == board[4] == board[5] !="_"
        column3 = board[6] == board[7] == board[8] !="_"
```            
Then if the fn finds any column with a common value, it will print the winner. This is given by the if elif statement,  
```python
        if column1:
            print("player " + board[0] + " wins the game.")
        elif column2:
            print("player " + board[3] + " wins the game.")
        elif column3:
            print("player " + board[6] + " wins the game.")
```                  
At last it will return the false value for the global variable "game_still_going".

The same coding will be given for the "check_raw()" and the "check_diagonal()" functions.

` Defining the tie() function ,`  
We will check the ```"_"``` in the board and print the statement for tie . it will also return the value False for the variable "game_still_going".  
```python
        def tie():
            global game_still_going
            if "_" not in board:
                print("it's a tie.")
                game_still_going = False
```     

`Defining flip_player() fn ,`  
if the current player is "x"  we will change it to "o"  
if the current player is "o"  we will change it to "x"  
```python
        def flip_player():
            global current_player
            if current_player == "x":
                current_player = "o"
            elif current_player == "o":
                current_player = "x"
```               

### At last we will call the ```play_game()``` fn

# WORKING :  

The game will start by reading the `play_game()` fn which will call the `display_board()` fn to display board.  
It will also start the while loop which will call the functions ,  
```python
1. handle_turn(current_player)
2. game_ended()
3. flip_player()  in a loop until the value of game_still_going is true.  
```       

The `handle_turn()` fn will take input from the user, checks if the input valid or not . If not , it asks the user for a new valid input .  
If the input is valid , it convert the position given into integer, subtract it by 1 to make it in a range from 1 to 9, and display the board again with the new input.

The `game_ended()` fn will call the `win()` fn which will call the `check_column()`, `check_raw()` and `check_diagonal()` fn.  
The `game_ended()` fn will also call the `tie()` fn

The `check_column()`, `check_raw()` and `check_diagonal()` fn will check each raw , each column and each diagonal for a common value, and if it finds any raw, column or diagonal with a common value  it will print the winner and end the game by giving a `False` value for `game_still_going`.  
The while loop in the `play_game()` fn will stop which will end the game.

The `tie()` fn will check the whole board for `"_"` .  
If it doesn’t find `"_"` in the board means the there is no space in the board and it will print `Tie.` and end the game.

The `flip_player()` fn will check the current_player variable.  
If the `current_player` is "X" it will change it to `"O"`.
If the `current_player` is "O" it will change it to `"X"`. 

The game will continue until `game_still_going = True`.  
The game will stop when `game_still_going` gets a False value from any of the functions used.

# EXECUTION : 

### 1. Save the file in “c” drive > user > your_python_folder
  
![path](https://user-images.githubusercontent.com/44708324/80893439-e8430480-8cef-11ea-913b-e53ad1e007ee.PNG)  

### 2. Give it a file name and save it with `.py` extension , in my case I have given it a name `tictactoe.py`
![saving the file](https://user-images.githubusercontent.com/44708324/80893549-ed548380-8cf0-11ea-8ccc-05811dc82189.PNG)

### 3. Open command prompt in your system and type the command “python filename.py” and press enter.
In my case I type “python tictactoe.py” ,

![command](https://user-images.githubusercontent.com/44708324/80893576-36a4d300-8cf1-11ea-8cbf-2ea9202998d0.PNG)

### 4. The game board will appear on your screen ,  
![game board](https://user-images.githubusercontent.com/44708324/80893635-d95d5180-8cf1-11ea-972f-c3aa61247f31.PNG)

### 5. Now you can start playing the game as much as you want :  
![x's turn](https://user-images.githubusercontent.com/44708324/80893664-0ad61d00-8cf2-11ea-9c16-8a1f363d38cc.PNG)

![o's turn](https://user-images.githubusercontent.com/44708324/80893696-3b1dbb80-8cf2-11ea-95d4-4b9c33f5aa47.PNG)

![game ended](https://user-images.githubusercontent.com/44708324/80893698-3f49d900-8cf2-11ea-865c-35e42fcba7a7.PNG)

---  
---

># Tic-Tac-Toe  with a GUI (Desktop application)

# [COMPLETE PROGRAM link](https://github.com/AMIT-ZING/Tic-Tac-Toe/blob/master/TIC-TAC-TOE_GUI.py)

#  EXPLANATION :
`First to import everything we will write :`  
```python
        from tkinter import *
```
`To get a window we will write the code :`  
```python
        root = Tk()
            < We will write everything between these two codes >
        root.mainloop()
```
`Giving a title :`
```python
        root.title("Tic Tac Toe")
```
`Creating buttons :`  

 We will add 9 buttons to the GUI window. We will determine color, text, bg, font, borderwidth, width and command for all the 9 buttons. Those buttons will be closed by grid will row and column determined. One example is given ,  
``` python     
        b1 = Button(text = " ", borderwidth = 15, bg = "gray", font=("Arial", 80, "bold"), width=3,          command = lambda : [flip_player(b1), check_if_win(b1)])
        b1.grid(row=0, column=0)
```

`Flipping players :`  

We will define “flip_player” variable and under that we will check the status of  “current_player” variable using  if – elif  statement and assign “X” and “Y” accordingly. We will also assign the current_player value to the “winner” variable to use it in the winning messagebox. We will also increment the “turn” variable to find out which turn is it.  We will also add a messagebox to show if the input is invalid.  
```python      
        def flip_player(button):
            global current_player
            global turn, winner
    
            # checking current_player for "X" value and assigning values to global variables accordingly
            if (current_player == "X") and button["text"]==" ": 
                button.config(text="X", fg="brown4")
                current_player = "O"
                winner = "X"
                turn = turn + 1

            # checking current_player for "Y" value and assigning values to global variables accordingly    
            elif (current_player == "O") and button["text"]==" ":
                button.config(text='O')
                current_player = "X"
                winner = "O"
                turn = turn + 1

            # displaying msg for invalid moves    
            else:
                messagebox.showinfo("INVALID !!", "CHOOSE ANOTHER POSITION FROM THE EMPTY SPACES !!")
``` 

`CHECKING FOR WINNER :`  

We will check the buttons for winning row, column or diagonal under an if-elif statement. It will also check the draw condition. We will add a messagebox to show the win or lose message. We will add another if-elif statement to check the winning row, column or diagonal and change the color of that row/column/diagonal.

```python
# checking if the game is won or is it a draw
def check_if_win(btn):
    
    # checking for win
    if b1["text"]==b2["text"]==b3["text"]!=" " or b4["text"]==b5["text"]==b6["text"]!=" " or                 b7["text"]==b8["text"]==b9["text"]!=" " or b1["text"]==b4["text"]==b7["text"]!=" " or b2["text"]==b5["text"]==b8["text"]!=" " or b3["text"]==b6["text"]==b9["text"]!=" " or b1["text"]==b5["text"]==b9["text"]!=" " or b3["text"]==b5["text"]==b7["text"]!=" ":
        
        # Checking the winning row, column or diagonal and giving it a different color
        if b1["text"]==b2["text"]==b3["text"]!=" ":
            b1["bg"]=b2["bg"]=b3["bg"]= "aquamarine"
        elif b4["text"]==b5["text"]==b6["text"]!=" ":
            b4["bg"]=b5["bg"]=b6["bg"]= "aquamarine"
        elif b7["text"]==b8["text"]==b9["text"]!=" ":
            b7["bg"]=b8["bg"]=b9["bg"]= "aquamarine"
        elif b1["text"]==b4["text"]==b7["text"]!=" ":
            b1["bg"]=b4["bg"]=b7["bg"]= "aquamarine"
        elif b2["text"]==b5["text"]==b8["text"]!=" ":
            b2["bg"]=b5["bg"]=b8["bg"]= "aquamarine"
        elif b3["text"]==b6["text"]==b9["text"]!=" ":
            b3["bg"]=b6["bg"]=b9["bg"]= "aquamarine"
        elif b1["text"]==b5["text"]==b9["text"]!=" ":
            b1["bg"]=b5["bg"]=b9["bg"]= "aquamarine"
        elif b3["text"]==b5["text"]==b7["text"]!=" ":
            b3["bg"]=b5["bg"]=b7["bg"]= "aquamarine"    
        
        messagebox.showinfo("WINNER", "PLAYER  " + winner + "  WON THE GAME.....")
        exit(0)
        root.destroy()

    # checking for draw    
    elif turn == 9:
        b1["bg"]=b2["bg"]=b3["bg"]=b4["bg"]=b5["bg"]=b6["bg"]=b7["bg"]=b8["bg"]=b9["bg"]="thistle1"
        messagebox.showinfo("DRAW!!", "IT'S A DRAW.....")
        exit(0)
        root.destroy()
```

# EXECUTION : 

## `1. Run the program :`  
For this GUI I’m using spyder :

![run](https://user-images.githubusercontent.com/44708324/80894148-3f4bd800-8cf6-11ea-8fe7-79bb7b006424.PNG)

---

## `2. X’s turn :`
![x's turn](https://user-images.githubusercontent.com/44708324/80894186-8df97200-8cf6-11ea-8884-f87fd5ff3ece.PNG)

---

## `3. O's turn :`
![o's turn](https://user-images.githubusercontent.com/44708324/80894199-acf80400-8cf6-11ea-804c-ed9760bdf96b.PNG)

---

# `WIN`
![winning row](https://user-images.githubusercontent.com/44708324/80894218-cf8a1d00-8cf6-11ea-9105-93c4bc4840f2.PNG)

---

# `DRAW`
![draw](https://user-images.githubusercontent.com/44708324/80894255-1d068a00-8cf7-11ea-9607-e8536f4e4b97.PNG)


> # WEB APPLICATION COMING SOON : 
