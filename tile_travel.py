#jass queen let's do this!
import random

# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'
game = True

def r_move(text):
    m = ['w','n','e','s']
    re = random.choice(m)
    print(text + str(re))
    return re

def r_yn(text):
    ans = ['y','n']
    re = random.choice(ans)
    print(text + str(re))
    return re

def play():
    play_ans = input("Play again (y/n): ")
    play_ans = play_ans.lower()
    if play_ans == 'n':
        return False
    else:
        return True

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
coins = 0       
def find_directions(col, row, coins,is_move):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        if is_move:
            get_coins()
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        if is_move:
            get_coins()
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        if is_move:
            get_coins()
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        if is_move:
            get_coins()
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def play_one_move(col, row, valid_directions):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = r_move("Direction: ")
    direction = direction.lower()
    
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
    return victory, col, row,1

def get_coins():
    answer = r_yn('Pull a lever (y/n): ')
    answer.lower()
    if answer == 'y':
        COIN_COUNTER.append(1)
        print('You received 1 coin, your total is now {}.'.format(sum(COIN_COUNTER)))

while game:
    # The main program starts here
    COIN_COUNTER = []
    MOVE_COUNTER = 0
    victory = False
    row = 1
    col = 1
    random.seed(input("Input seed: "))

    valid_directions = NORTH
    print_directions(valid_directions)

    while not victory:
        is_move = 0
        victory, col, row, is_move = play_one_move(col, row, valid_directions)
        MOVE_COUNTER += is_move
        if victory:
            print("Victory! Total coins {}. Moves {}.".format(sum(COIN_COUNTER),MOVE_COUNTER))
            game = play()
        else:
            valid_directions = find_directions(col, row, coins, is_move)
            print_directions(valid_directions)