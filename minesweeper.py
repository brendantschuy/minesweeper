from tkinter import *
import numpy as np
import random as rand
import time

class Board:
    def __init__(self, rows, cols, mines, canvas):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.canvas = canvas
        rand.seed()
        self.createBoard()
        self.drawBoard()

    def __str__(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.board[i][j])
            print('\n')

    def createBoard(self):
        self.board = [[Tile(False, i * 10 + j) for j in range(self.cols)] for i in range(self.rows)]
        mineHashes = []
        for i in range(self.mines):
            x = rand.randint(0, self.rows - 1)
            y = rand.randint(0, self.cols - 1)
            mineHash = x * 10 + y
            if mineHash not in mineHashes:
                self.board[x][y].createMine(mineHash)
                mineHashes.append(mineHash)
            else:
                i = i - 1
        print(mineHashes)
        self.genNumbers(mineHashes)
            #self.getNumbers(mineHashes)

    def genNumbers(self, hashes):
        for i in range(self.rows):
            for j in range(self.cols):
                if(self.board[i][j].hasMine == False):
                    adjacency = [-11, -10, -9, -1, 1, 9, 10, 11]
                    adjacentHashes = [x + self.board[i][j].hash for x in adjacency]
                    print(adjacentHashes)
                    self.board[i][j].setNum(len([value for value in adjacentHashes if value in hashes]))
                else:
                    num = 0

    def drawBoard(self):
        for i in range(self.rows):
            for j in range(self.cols):
                thisTile = self.board[i][j]
                color = thisTile.color
                if(thisTile.flagged == True and thisTile.isVisible == False):
                    self.canvas.createText((i * 40 + 20, j * 40 + 20), text="X")
                self.canvas.create_rectangle(i * 40, j * 40, (i + 1) * 40, (j + 1) * 40, fill=color, tags="square" + str(thisTile.hash))
                if(thisTile.isVisible == True):
                    self.canvas.create_text((i * 40 + 20, j * 40 + 20), text=thisTile.numAdjacent)
                self.canvas.tag_bind("square" + str(thisTile.hash),"<Button-1>",thisTile.clicked)
                self.canvas.tag_bind("square" + str(thisTile.hash),"x",thisTile.flagged)
        self.canvas.after(50, self.drawBoard)

    def numAdjacent(self, i, j):
        return "0"
        

class Tile:
    def __init__(self, hasMine, myHash):
        self.hasMine = hasMine
        self.numAdjacent = 0
        self.isVisible = False
        self.hash = myHash
        self.color = "#AAAAAA"

    def createMine(self, mineHash):
        self.hasMine = True
        self.hash = mineHash

    def isMine(self):
        if(self.hasMine == True):
            return 1
        else:
            return 0

    def getColor(self):
        if(self.hasMine == True and self.isVisible == True):
            return "#444444"
        elif(self.isVisible == True):
            return "#DDDDDD"
        else: #still not visible (default value)
            return "#AAAAAA"

    def setNum(self, num):
        self.numAdjacent = num

    def clicked(self, key):
        print(f"Clicked {self.hash}")
        if(self.hasMine == True):
            self.color="#444444"
        else:
            self.color="#DDDDDD"
        self.isVisible = True

    def flagged(self):
        print(f"Flagged {self.hash}")
        self.flagged = not self.flagged

master = Tk()
w = Canvas(master, width=200, height=200)
w.pack()
b = Board(5, 5, 10, w)
master.mainloop()


        
