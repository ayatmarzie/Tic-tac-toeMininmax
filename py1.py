import sys
import time
from math import inf
import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
#from puring import abminimax
sign = 0
you, computer = 'O', 'X'
global board
board = [
    [ ' ', ' ', ' ' ],
    [ ' ', ' ', ' ' ],
    [ ' ', ' ', ' ' ]
    ]
totalalphabetatime=0.00
def victory(board) :
   
    conditions = [[board[0][0], board[0][1], board[0][2]],
                     [board[1][0], board[1][1], board[1][2]],
                     [board[2][0], board[2][1], board[2][2]],
                     [board[0][0], board[1][0], board[2][0]],
                     [board[0][1], board[1][1], board[2][1]],
                     [board[0][2], board[1][2], board[2][2]],
                     [board[0][0], board[1][1], board[2][2]],
                     [board[0][2], board[1][1], board[2][0]]]
    if [you, you, you] in conditions:
        return 1
    elif [computer, computer, computer] in conditions:
        return -1
def count(board):
    countb=0
    blank = []
    for i in range(3) :
        for j in range(3) :
            if(board[i][j]==' ' ):
                countb+=1
                blank.append([i, j])

    return countb,blank
def isfull():
    flag = True
    for i in board:
        if(i.count(' ') > 0):
            flag = False
    return flag
def winner(b, l):
    conditions = [[board[0][0], board[0][1], board[0][2]],
                     [board[1][0], board[1][1], board[1][2]],
                     [board[2][0], board[2][1], board[2][2]],
                     [board[0][0], board[1][0], board[2][0]],
                     [board[0][1], board[1][1], board[2][1]],
                     [board[0][2], board[1][2], board[2][2]],
                     [board[0][0], board[1][1], board[2][2]],
                     [board[0][2], board[1][1], board[2][0]]]

    if [l, l, l] in conditions:
        return True

    return False






def minimax(board, depth, isMax) :
    countb,blank=count(board)
    score = victory(board)
    if (score ) :
        return score
    if (countb==0) :
        return 0

    if (isMax) :    
        best = -inf
 
    
        for cell in blank:
                 
                    
            board[cell[0]][cell[1]] = you
 
        
            best = max( best, minimax(board,depth + 1,not isMax) )
 
    
            board[cell[0]][cell[1]] = ' '
        return best
 
    else :
        best = inf
 
        for cell in blank:
            board[cell[0]][cell[1]] = computer
 
            best = min(best, minimax(board, depth + 1, not isMax))
 
                    # Undo the move
            board[cell[0]][cell[1]] = ' '
        return best
 
# This will return the best possible move for the you
def findBestMove() :
    global  totalalphabetatime
    start_time = time.time()
    bestVal = -inf
    bestMove = (-1, -1)
    countb,blank=count(board)
    if(countb):
        for cell in blank:
             
            board[cell[0]][cell[1]] = you
            moveVal = minimax(board, 0, False)

            board[cell[0]][cell[1]] = ' '
 
            if (moveVal > bestVal) :               
                    bestMove = (cell[0], cell[1])
                    bestVal = moveVal
        totalalphabetatime+=(time.time() - start_time)
        print("--- %s seconds ---" % (time.time() - start_time))
        return bestMove
        


  
# Configure text on button while playing with system
def get_text_minimax(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Player won the match")
    elif winner(board, "O"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Computer won the match")
    elif(isfull()):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Tie Game", "Tie Game")
    if(x):
        if sign % 2 != 0:
            move = findBestMove()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_minimax(move[0], move[1], gb, l1, l2)
  
# Create the GUI of game board for play along with system
def gameboard_minimax(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_minimax, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()
  
# Initialize the game board to play with system
def withminimax(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="Player : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text = "Computer : O",
                width = 10, state = DISABLED)
      
    l2.grid(row = 2, column = 1)
    gameboard_minimax(game_board, l1, l2)
'''def get_text_ab(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Player won the match")
    elif winner(board, "O"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Computer won the match")
    elif(isfull()):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Tie Game", "Tie Game")
    if(x):
        if sign % 2 != 0:
            move = pvc()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_ab(move[0], move[1], gb, l1, l2)
  
# Create the GUI of game board for play along with system
def gameboard_ab(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_minimax, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()   
def withab(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="Player : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text = "Computer : O",
                width = 10, state = DISABLED)
      
    l2.grid(row = 2, column = 1)
    gameboard_ab(game_board, l1, l2)
   
'''

def play():
    menu = Tk()
    menu.geometry("250x250")
    menu.title("Tic Tac Toe")
    wminimax = partial(withminimax, menu)
    #wab = partial(withab, menu) 
    head = Button(menu, text = "---Welcome to tic-tac-toe---",
                  activeforeground = 'red',
                  activebackground = "yellow", bg = "red", 
                  fg = "yellow", width = 500, font = 'summer', bd = 5)
      
    B1 = Button(menu, text = "Minimax", command = wminimax, 
                activeforeground = 'red',
                activebackground = "yellow", bg = "red", 
                fg = "yellow", width = 500, font = 'summer', bd = 5)
    '''B2 = Button(menu, text = "alphabeta", command = wab, 
                activeforeground = 'red',
                activebackground = "yellow", bg = "red", 
                fg = "yellow", width = 500, font = 'summer', bd = 5)
       
    '''
    head.pack(side = 'top')
    B1.pack(side = 'top')
    #B2.pack(side = 'top')
    menu.mainloop()
  
if __name__ == '__main__':
        play()
        print("--- %s seconds ---" % totalalphabetatime)