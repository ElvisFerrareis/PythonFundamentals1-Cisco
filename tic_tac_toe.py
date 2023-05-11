from random import randrange

positions = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}


def display_board(board):
    display = """
    +-------+-------+-------+
    |       |       |       |
    |   """ + str(board[0][0]) + """   |   """ + str(board[0][1]) + """   |   """ + str(board[0][2]) + """   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   """ + str(board[1][0]) + """   |   """ + str(board[1][1]) + """   |   """ + str(board[1][2]) + """   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   """ + str(board[2][0]) + """   |   """ + str(board[2][1]) + """   |   """ + str(board[2][2]) + """   |
    |       |       |       |
    +-------+-------+-------+
    """
    print(display)


def enter_move(board):
    right_move = False
    while not right_move:
        try:
            move = int(input("Informe a posição, entre 1 e 9, em que deseja fazer o movimento: "))
            free_positions = make_list_of_free_fields(board)
            if free_positions[move-1] == 1:
                board[positions[move][0]][positions[move][1]] = 'O'
                right_move = True
            else:
                print("Posição já ocupada!\nPor favor, escolha uma posição livre.")
        except ValueError:
            print("Digite apenas números inteiros!")
            continue
        except IndexError:
            print("Posição inválida!\nSomente são aceitos números entre 1 e 9.")
    return board


def make_list_of_free_fields(board):
    free_fields = []
    for i in range(1, 10):
        if board[positions[i][0]][positions[i][1]] in ['X', 'O']:
            free_fields.append(0)
        else:
            free_fields.append(1)
    return free_fields


def victory_for(board):
    if ["X", "X", "X"] in [[str(board[0][x]) for x in range(3)],
                               [str(board[1][x]) for x in range(3)],
                               [str(board[2][x]) for x in range(3)],
                               [str(board[x][0]) for x in range(3)],
                               [str(board[x][1]) for x in range(3)],
                               [str(board[x][2]) for x in range(3)],
                               [str(board[x][x]) for x in range(3)],
                               [str(board[x][2 - x]) for x in range(3)]]:
        return "X"
    elif ["O", "O", "O"] in [[str(board[0][x]) for x in range(3)],
                                 [str(board[1][x]) for x in range(3)],
                                 [str(board[2][x]) for x in range(3)],
                                 [str(board[x][0]) for x in range(3)],
                                 [str(board[x][1]) for x in range(3)],
                                 [str(board[x][2]) for x in range(3)],
                                 [str(board[x][x]) for x in range(3)],
                                 [str(board[x][2 - x]) for x in range(3)]]:
        return "O"
    else:
        return ""


def draw_move(board):
    victorious = ""
    turn = 0
    display_board(board)
    while victorious == "" and turn < 8:
        if not turn % 2:
            enter_move(board)
        else:
            valid_move = False
            while not valid_move:
                computer_move = randrange(8) + 1
                free_positions = make_list_of_free_fields(board)
                if free_positions[computer_move] == 1:
                    board[positions[computer_move + 1][0]][positions[computer_move + 1][1]] = "X"
                    valid_move = True
        display_board(board)
        if turn >= 4:
            victorious = victory_for(board)
        turn += 1

    if victorious in ["X", "O"]:
        return "Jogador " + victorious + " venceu o jogo!"
    else:
        return "O jogo terminou empatado!"


board = [[row + (3 * column) for row in range(1, 4)] for column in range(0, 3)]

board[1][1] = "X"

print(draw_move(board))