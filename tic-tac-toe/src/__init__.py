from classes import Player, Board




if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe")
    name = input("What's the name of player 1?: ")
    sign = input(f"Which sign does {name} want to use?: ")
    p1 = Player(name, sign)

    name = input("What's the name of player 2?: ")
    sign = input(f"Which sign does {name} want to use?: ")
    p2 = Player(name, sign)

    board = Board()
    while True:
        print(f"{p1.name}'s Turn")
        p1.pickSquare(board)

        print(f"{p2.name}'s Turn")
        p2.pickSquare(board)