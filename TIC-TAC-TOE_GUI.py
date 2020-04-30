# ======================== TIC TAC TOE using TKINTER ============================

# ===== CONTENTS: ====== 

# A title : tic tac toe
# Creating 9 buttons ( arranged in 3 columns and 3 rows )
# Manage turn : fliping players and assigning "X" and "O" accordingly 
# Logic : win and draw
# MessageBox to display win and loss 
# Improving the GUI appearance :
             # changing the color of winning row, column or diagonal
             # changing the color of the buttons when it's a win
             # giving color to the text "X' and "O"
             # improving the size of the button and the texts


from tkinter import *
from tkinter import messagebox

# ==========GLOBAL VARIABLES==========
current_player = "X"
turn = 0
winner = " "


# checking if the game is won or is it a draw
def check_if_win(btn):
    
    # checking for win
    if b1["text"]==b2["text"]==b3["text"]!=" " or b4["text"]==b5["text"]==b6["text"]!=" " or b7["text"]==b8["text"]==b9["text"]!=" " or b1["text"]==b4["text"]==b7["text"]!=" " or b2["text"]==b5["text"]==b8["text"]!=" " or b3["text"]==b6["text"]==b9["text"]!=" " or b1["text"]==b5["text"]==b9["text"]!=" " or b3["text"]==b5["text"]==b7["text"]!=" ":
        
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
        
    
# function for fliping the players from "x" to "y" or from "y" to "x"             
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
        
        
# Making a tkinter GUI window
root = Tk()

# Giving a title
root.title("Tic Tac Toe")


# Adding buttons
b1 = Button(text = " ", borderwidth = 15, bg = "gray", font=("Arial", 80, "bold"), width=3, command = lambda : [flip_player(b1), check_if_win(b1)])
b1.grid(row=0, column=0)
b2 = Button(text = " ", borderwidth = 15, bg = "gray", font=("Arial", 80, "bold"), width=3, command = lambda : [flip_player(b2), check_if_win(b1)])
b2.grid(row=0, column=1)
b3 = Button(text = " ", borderwidth = 15, bg = "gray", font=("Arial", 80, "bold"), width=3, command = lambda : [flip_player(b3), check_if_win(b1)])
b3.grid(row=0, column=2)
b4 = Button(text = " ", borderwidth = 15, bg = "gray", font=("Arial", 80, "bold"), width=3, command = lambda : [flip_player(b4), check_if_win(b1)])
b4.grid(row=1, column=0)
b5 = Button(text = " ", borderwidth = 15, bg = "gray", font=("Arial", 80, "bold"), width=3, command = lambda : [flip_player(b5), check_if_win(b1)])
b5.grid(row=1, column=1)
b6 = Button(text = " ", borderwidth = 15, bg = "gray", font=("Arial", 80, "bold"), width=3, command = lambda : [flip_player(b6), check_if_win(b1)])
b6.grid(row=1, column=2)
b7 = Button(text = " ", borderwidth = 15, bg = "gray", font=("Arial", 80, "bold"), width=3, command = lambda : [flip_player(b7), check_if_win(b1)])
b7.grid(row=2, column=0)
b8 = Button(text = " ", borderwidth = 15, bg = "gray", font=("Arial", 80, "bold"), width=3, command = lambda : [flip_player(b8), check_if_win(b1)])
b8.grid(row=2, column=1)
b9 = Button(text = " ", borderwidth = 15, bg = "gray", font=("Arial", 80, "bold"), width=3, command = lambda : [flip_player(b9), check_if_win(b1)])
b9.grid(row=2, column=2)


# calling the main loop(calling GUI window)
root.mainloop()