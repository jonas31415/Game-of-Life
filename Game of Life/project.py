# ============================================================================ #
# Final Project for Introduction to Python, Winter 2021/2022
# 
# Names
#     Jonas Lippl, Mat.Nr. 2101758

#John Conway's Game of Life (with periodic boundary conditions)
#Creating a Graphical User Interface with tkinter

import tkinter as tk
import time

size=10

root=tk.Tk(className="John Conway's Game of Life")

"""========================="""
"""Create Start/Stop-Button:"""
"""========================="""
class startButton:
    def __init__(self):
        self.button=tk.Button(root, text="Start", command=lambda:self.start(), bg="red")
        self.bool=True
    def start(self):
        self.bool=True
        #while(self.bool):
        for t in range(0,1):
            #print(t)
            evolve(fieldButtons, size)
            time.sleep(0.5)

#python coroutines
#onclick von start ruft asyncio auf
#docs.python.org asyncio-task


startBtn=startButton()
startBtn.button.grid(columnspan=2,rowspan=1, column=0, row=size+1)

class stopButton:
    def __init__(self):
        self.button=tk.Button(root, text="Stop", command=lambda:self.Stop(), bg="red")
    def Stop():
        startBtn.bool=False

stopBtn=stopButton()
stopBtn.button.grid(columnspan=2,rowspan=1, column=2, row=size+1)


"""============="""
"""Create Field:"""
"""============="""
fieldButtons=[]

class buttons:
    def __init__(self, x=0, y=0):
        self.button=tk.Button(root, text=" ", command=lambda:self.onclick(), bg="grey")
        self.x=x
        self.y=y
        self.color=0
        self.born=0
        self.die=0
    def onclick(self):
        self.button.configure(bg="blue")
        self.color=1

for i in range(0,size):
    fieldButtons.append([])
    for j in range(0,size):
        button=buttons(i, j)
        fieldButtons[i].append(button)
        fieldButtons[i][j].button.grid(columnspan =1,rowspan=1, column=i, row=j)


"""==============================="""
"""Create Functions for execution:"""
"""==============================="""
def countNeighbours(fM, row, col, size):
    #fM is the field Matrix
    if row==size-1 and col==size-1:  #right lower corner
        count=fM[row-1][col-1].color+fM[row-1][col].color+fM[row-1][col-size+1].color+fM[row][col-1].color+fM[row][col-size+1].color+fM[row-size+1][col-1].color+fM[row-size+1][col].color+fM[row-size+1][col-size+1].color 
    elif row==size-1 and col==0:  #left lower corner
        count=fM[row-1][col+size-1].color+fM[row-1][col].color+fM[row-1][col+1].color+fM[row][col+size-1].color+fM[row][col+1].color+fM[row-size+1][col+size-1].color+fM[row-size+1][col].color+fM[row-size+1][col+1].color    
    elif row==0 and col==0:   #left upper corner
        count=fM[row+size-1][col+size-1].color+fM[row+size-1][col].color+fM[row+size-1][col+1].color+fM[row][col+size-1].color+fM[row][col+1].color+fM[row+1][col+size-1].color+fM[row+1][col].color+fM[row+1][col+1].color
    elif row==0 and col==size-1:  #right upper corner
        count=fM[row+size-1][col-1].color+fM[row+size-1][col].color+fM[row+size-1][col-size+1].color+fM[row][col-1].color+fM[row][col-size+1].color+fM[row+1][col-1].color+fM[row+1][col].color+fM[row+1][col-size+1].color
    elif row==0:    #upper edge
        count=fM[row+size-1][col-1].color+fM[row+size-1][col].color+fM[row+size-1][col+1].color+fM[row][col-1].color+fM[row][col+1].color+fM[row+1][col-1].color+fM[row+1][col].color+fM[row+1][col+1].color
    elif row==size-1:   #lower edge
        count=fM[row-1][col-1].color+fM[row-1][col].color+fM[row-1][col+1].color+fM[row][col-1].color+fM[row][col+1].color+fM[row-size+1][col-1].color+fM[row-size+1][col].color+fM[row-size+1][col+1].color  
    elif col==0:    #left edge
        count=fM[row-1][col+size-1].color+fM[row-1][col].color+fM[row-1][col+1].color+fM[row][col+size-1].color+fM[row][col+1].color+fM[row+1][col+size-1].color+fM[row+1][col].color+fM[row+1][col+1].color
    elif col==size-1:   #right edge
        count=fM[row-1][col-1].color+fM[row-1][col].color+fM[row-1][col-size+1].color+fM[row][col-1].color+fM[row][col-size+1].color+fM[row+1][col-1].color+fM[row+1][col].color+fM[row-1][col-size+1].color
    else:   #anything else
        count=-fM[row][col].color
        for a in range(-1,2):
            for b in range(-1,2):
                count+=fM[row+a][col+b].color
        
    return count

def evolve(fM, size):
    #fm is the fieldMatrix with all the buttons
    #0: dead, 1: alive
    for i in range(0, size):
        for j in range(0,size):
            x=countNeighbours(fM, i, j, size)
            #print(x)
            if fM[i][j].color==0 and x==3:
                fM[i][j].born=1
            elif fM[i][j].color==1 and x<2:
                fM[i][j].die=1
            elif fM[i][j].color==1 and 2<=x<=3:
                fM[i][j].color=1
            elif fM[i][j].color==1 and x>3:
                fM[i][j].die=1
            else:
                fM[i][j].color=0

    for i in range(0, size):
        for j in range(0,size):
            if fM[i][j].color==1 and fM[i][j].die==1:
                fM[i][j].button.configure(bg="grey")
                fM[i][j].color=0
            elif fM[i][j].color==0 and fM[i][j].born==1:
                fM[i][j].button.configure(bg="blue")
                fM[i][j].color=1
            fM[i][j].die=0
            fM[i][j].born=0

root.mainloop()