from random import randint, choice
from time import sleep

# -------------------------------------------------------------------

game_page = [
#    1    2    3
    '_', '_', '_', # a
    '_', '_', '_', # b
    '_', '_', '_' # c
]

# -------------------------------------------------------------------

def printer():
    print(game_page[0], game_page[1], game_page[2])
    print(game_page[3], game_page[4], game_page[5])
    print(game_page[6], game_page[7], game_page[8])

# -------------------------------------------------------------------

def game():
    printer()
    while True:
        user_move = input("enter number: ")
        if game_page[int(user_move)-1] == "_":
            game_page[int(user_move)-1] = "O"
            break
    result , winner = checker()
    if result:
        return winner

    while True:
        computer_choice = choice(game_page)
        if computer_choice == "_":
            game_page[game_page.index(computer_choice)] = "X"
            break

    result , winner = checker()
    if result:
        return winner
    
    return None


# -------------------------------------------------------------------

def checker():
    for i in range(0, 9, 3):
        if game_page[i] != "_":
            if game_page[i] == game_page[i+1] == game_page[i+2]:
                return True , game_page[i]
            
    for i in range(3):
        if game_page[i] != "_":
            if game_page[i] == game_page[i+3] == game_page[i+6]:
                return True , game_page[i]
            
    if game_page[0] != "_":
        if game_page[0] == game_page[4] == game_page[8]:
            return True , game_page[0]
        
    if game_page[2] != "_":
        if game_page[2] == game_page[4] == game_page[6]:
            return True , game_page[0]
        
    return None , "_"
    
# -------------------------------------------------------------------

res = "no one"
while True:
    res = game()
    if res != None:
        break

printer()
print(res, "is the winner!!!!")



