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
    print("      1        2        3")
    print("a","[",game_page[0] ,"]","[", game_page[1],"]","[",game_page[2],"]", sep="  ", end="\n\n")
    print("b","[",game_page[3] ,"]","[", game_page[4],"]","[",game_page[5],"]", sep="  ", end="\n\n")
    print("c","[",game_page[6] ,"]","[", game_page[7],"]","[",game_page[8],"]", sep="  ", end="\n\n")
    print("-" * 40)

# -------------------------------------------------------------------

def game():
    print("-"*16)
    while True:
        print("-"*16)
        print("---your turn ---")
        print("-"*16)
        user_move = input("enter your move: ")
        if user_move == "a1":
            user_move = 1
        elif user_move == "a2":
            user_move = 2
        elif user_move == "a3":
            user_move = 3
        elif user_move == "b1":
            user_move = 4
        elif user_move == "b2":
            user_move = 5
        elif user_move == "b3":
            user_move = 6
        elif user_move == "c1":
            user_move = 7
        elif user_move == "c2":
            user_move = 8
        elif user_move == "c3":
            user_move = 9

        if game_page[int(user_move)-1] == "_":
            game_page[int(user_move)-1] = "O"
            break
    result , winner = checker()
    if result:
        return winner

    printer()

    print("-"*16)
    print("-computer turn -")
    print("-"*16)

    sleep(1.5)

    while True:
        computer_choice = choice(game_page)
        if computer_choice == "_":
            game_page[game_page.index(computer_choice)] = "X"
            break

    result , winner = checker()
    if result:
        return winner
    
    printer()

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
printer()
while True:
    res = game()
    if res != None:
        break
printer()
print("="*16)
if res == "O":
    print("you win!!!!!")
else:
    print("you lose!!!!")




