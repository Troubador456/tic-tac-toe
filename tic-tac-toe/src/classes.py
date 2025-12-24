class Board:
    def __init__(self):
        self.spaces = [[None,None,None],[None,None,None],[None,None,None]]
    def printFull(self):
        print("----------------------")
        for r in self.spaces:
            print(f"{r[0]}|{r[1]}|{r[2]}")
            print("------------------------")
    def fill(self, r, c, sign):
        self.spaces[r][c] = sign

class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign
    def pickSquare(self, board: 'Board') -> None:
        print("Here is the board")
        board.printFull()
        row = int(input("Which row?: "))
        col = int(input("Which column?: "))
        row-=1
        col-=1
        if 0 <= row <= 2 and 0 <= col <= 2:
            if board.spaces[row][col] is None:
                board.fill(row,col,self.sign)
            else:
                print("Square has already been filled")
                return self.pickSquare(board)
        else:
            print("Bad input")
            return self.pickSquare(board)
        if [self.sign, self.sign, self.sign] in board.spaces or (self.sign in board.spaces[0] and self.sign in board.spaces[1] and self.sign in board.spaces[2]):
            print(f"{self.name} has won")
            exit()  
        endsInLoop = False
        for r in range(3):
            for c in board.spaces[r]:
                if c is None:
                    endsInLoop = True
                    break
            if endsInLoop:
                break
            if r == 2:
                print("Draw")
                exit()
        
                


