#  Following code takes a matrix and prints the it into the game board
def print_board(game_matrix):
    print("---------")
    print("|", game_matrix[0][0], game_matrix[0][1], game_matrix[0][2], "|")
    print("|", game_matrix[1][0], game_matrix[1][1], game_matrix[1][2], "|")
    print("|", game_matrix[2][0], game_matrix[2][1], game_matrix[2][2], "|")
    print("---------")


#  Following code takes a string and converts it into a 3 * 3 matrix
def create_matrix(game_list):
    if len(game_list) > 9:
        print("Input string is too long")
        exit()
    else:
        game_matrix = [[game_list[0], game_list[1], game_list[2]],
                       [game_list[3], game_list[4], game_list[5]],
                       [game_list[6], game_list[7], game_list[8]]]
    return game_matrix


#  This code takes the user coordinates and matrix and returns the value in the chosen cell
def check_matrix(coord1, coord2, matrix):
    current_value = matrix[(coord1 - 1)][(coord2 - 1)]
    return current_value


#  This code takes the game_matrix and converts it to a string that can be used with other functions
def create_string(game_matrix):
    new_list = ""
    for row_ in game_matrix:
        for i in row_:
            new_list = new_list + i
    return new_list


#  This code takes the user move and player string "X" or "O",
#  updates the board and prints the new board
def update_board(user_move, player):
    global game_matrix
    game_matrix[user_move[0] - 1][user_move[1] - 1] = player
    print_board(game_matrix)


#  This function requests a user move and performs all error checks on the move
#  before passing it back as 2 integer coordinates
def request_user_move(player):
    global game_matrix
    user_move = input(player + ": Enter Move").split()  # Should be a string of 2 numbers between 1 and 3
    accepted_moves = ["1", "2", "3"]
    if len(user_move) != 2:
        print("You have not entered 2 coordinates, please enter 2 numbers separated by a whitespace i.e. 1 3")
        return request_user_move(player)
    if "".join(user_move).isnumeric() is False:
        print("You should enter numbers!")
        return request_user_move(player)
    for coordinate in user_move:
        if coordinate not in accepted_moves:
            print("Coordinates should be from 1 to 3!")
            return request_user_move(player)
    chosen_cell_value = check_matrix(int(user_move[0]), int(user_move[1]), game_matrix)
    if chosen_cell_value == "X" or chosen_cell_value == "O":
        print("This cell is occupied! Choose another one!")
        return request_user_move(player)
    return [int(user_move[0]), int(user_move[1])]


def check_game_won(game_matrix):
    win_combinations = [[0, 1, 2],
                        [3, 4, 5],
                        [6, 7, 8],
                        [0, 3, 6],
                        [1, 4, 7],
                        [2, 5, 8],
                        [0, 4, 8],
                        [6, 4, 2]]
    x_win = False
    o_win = False
    game_l = [game_matrix[0][0], game_matrix[0][1], game_matrix[0][2],
              game_matrix[1][0], game_matrix[1][1], game_matrix[1][2],
              game_matrix[2][0], game_matrix[2][1], game_matrix[2][2]]
    for x in win_combinations:
        if game_l[x[0]] == "X" and game_l[x[1]] == "X" and game_l[x[2]] == "X":
            x_win = True
        if game_l[x[0]] == "O" and game_l[x[1]] == "O" and game_l[x[2]] == "O":
            o_win = True

    if not -1 <= game_l.count("X") - game_l.count("O") <= 1:
        print("Impossible")
        exit()
    elif x_win is True and o_win is True:
        print("Impossible")
        exit()
    elif x_win is True and o_win is False:
        print("X wins")
        exit()
    elif x_win is False and o_win is True:
        print("O wins")
        exit()
    elif game_l.count(" ") > 0 or game_l.count("_") > 0:
        return "continue"
    else:
        print("Draw")
        exit()


# Modify the code to work with matrix ongoing
game_start = list("_________")
game_matrix = create_matrix(game_start)
print_board(game_matrix)

while check_game_won(game_matrix) == "continue":
    user_coord = request_user_move("X")
    update_board(user_coord, "X")
    check_game_won(game_matrix)
    user_coord = request_user_move("O")
    update_board(user_coord, "O")

# These win combinations where written for the list need to write this into a check_game function
