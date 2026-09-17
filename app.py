global board
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def printBoard():
    toPrint=""
    for i in range(9):
        toPrint = toPrint + "[" + str(board[i]) + "]"
        if i % 3 == 2:
            toPrint=toPrint+"\n"
    return toPrint

def gameloop(play):
    gameOver=False
    while play==True and gameOver==False:

        print(printBoard())
        xMove=int(input("Xs move: "))
        board[board.index(xMove)]="X"
        print(printBoard())

        if board[0]=="X" and board[1]=="X" and board[2]=="X" or board[3]=="X" and board[4]=="X" and board[5]=="X" or board[6]=="X" and board[7]=="X" and board[8]=="X":
            print("X Wins!!")
            gameOver=True
        if board[0] == "X" and board[3] == "X" and board[6] == "X" or board[1] == "X" and board[4] == "X" and board[7] == "X" or board[2] == "X" and board[5] == "X" and board[8] == "X":
            print("X Wins!!")
            gameOver=True
        if board[0] == "X" and board[4] == "X" and board[8] == "X" or board[2] == "X" and board[4] == "X" and board[6] == "X":
            print("X Wins!!")
            gameOver=True

        if gameOver==False:
            oMove = int(input("0s move: "))
            board[board.index(oMove)] = "0"

        if board[0]=="0" and board[1]=="0" and board[2]=="0" or board[3]=="0" and board[4]=="0" and board[5]=="0" or board[6]=="0" and board[7]=="0" and board[8]=="0":
            print("0 Wins!!")
            gameOver = True
        if board[0] == "0" and board[3] == "0" and board[6] == "0" or board[1] == "0" and board[4] == "0" and board[7] == "0" or board[2] == "0" and board[5] == "0" and board[8] == "0":
            print("0 Wins!!")
            gameOver = True
        if board[0] == "0" and board[4] == "0" and board[8] == "0" or board[2] == "0" and board[4] == "0" and board[6] == "0":
            print("0 Wins!!")
            gameOver = True

gameloop(True)
again=str(input(("Play again? (Y/N) ")))
if again.lower()=="y":
    gameloop(True)
else:
    gameLoop(False)

