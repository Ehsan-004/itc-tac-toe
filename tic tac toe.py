from random import randint, choice

game_page = [
    # 1    2    3
    ['-', '-', '-'], # a
    ['-', '-', '-'], # b
    ['-', '-', '-']  # c
]
def printer(game_p):
    print(game_p[0][0], game_p[0][1], game_p[0][2] , sep="\t")
    print(game_p[1][0], game_p[1][1], game_p[1][2] , sep="\t")
    print(game_p[2][0], game_p[2][1], game_p[2][2] , sep="\t")
    print("-" * 40)

def game():
    printer(game_page)
    print("your turn: ")
    user_input = input("enter where: ")
    if user_input[0] == "a":
        if user_input[1] == '1':
            game_page[0][0] = 'O'
        if user_input[1] == '2':
            game_page[0][1] = 'O'
        if user_input[1] == '3':
            game_page[0][2] = 'O'

    elif user_input[0] == "b":
        if user_input[1] == '1':
            game_page[0][0] = 'O'
        if user_input[1] == '2':
            game_page[0][1] = 'O'
        if user_input[1] == '3':
            game_page[0][2] = 'O'

    elif user_input[0] == "c":
        if user_input[1] == '1':
            game_page[0][0] = 'O'
        if user_input[1] == '2':
            game_page[0][1] = 'O'
        if user_input[1] == '3':
            game_page[0][2] = 'O'

    printer(game_page)

    comp_choose = False
    while not comp_choose :
        ind_khat_c = randint(0, 2) # index of the list in gamepage
        ind_khane_c = randint(0, 2) 
        khane_c = game_page[ind_khat_c][ind_khane_c]
        if khane_c == '-':
            game_page[ind_khat_c][ind_khane_c] = 'X'
            comp_choose = True

    printer(game_page)

# ---------------------------------------------------------------------------

winner = None

while True:
    game()

    if game_page[0][0] == game_page[1][1] == game_page[2][2] == 'X':
        winner = "computer"
        break

    elif game_page[0][0] == game_page[1][1] == game_page[2][2] == 'O':
        winner = "user"
        break

    elif game_page[0][2] == game_page[1][1] == game_page[2][0] == 'X':
        winner = "computer"
        break

    elif  game_page[0][2] == game_page[1][1] == game_page[2][0] == 'O':
        winner = "user"

    for i in range (3):
        if (game_page[i][0] == "X" and game_page[i][1] == "X" and game_page[i][2] == "X"):
            winner = "computer"
            break

        elif  (game_page[i][0] == "O" and game_page[i][1] == "O" and game_page[i][2] == "O"):
            winner = "user"
            break

    for i in range (3):
        if (game_page[0][i] == "X" and game_page[1][i] == "X" and game_page[2][i] == "O"):
            winner = "computer"
            break
        elif (game_page[0][i] == "O" and game_page[1][i] == "O" and game_page[2][i] == "X"):
            winner = "user"
            break

print("-" * 40)

print("end of game!!!")

print(winner , "won the game!!!")
