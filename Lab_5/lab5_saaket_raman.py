# The code for this project represents my own, independent work. I have neither given nor received help on this assignment from other students.
# Saaket Raman

from random import randint

snake_start = []
snake_end = []
ladder_start = []
ladder_end = []

def create_board(snake_start, snake_end, ladder_start, ladder_end):
    usedSpaces = [0]
    
    # Generating Snakes
    numSnakes = randint(2,8)

    i = 2
    while i <= numSnakes:
        spaces = list((randint(2,63), randint(2,63)))
        spaces.sort()

        if (spaces[0] != spaces[1]) and (spaces[0] not in usedSpaces) and (spaces[1] not in usedSpaces):
            snake_start.append(spaces[1])
            snake_end.append(spaces[0])
            usedSpaces += spaces
            i += 1
        else:
            i = i
        
    # Generating Ladders
    numLadders = randint(2,8)

    i = 2
    while i <= numLadders:
        spaces = list((randint(2,63), randint(2,63)))
        spaces.sort()

        if (spaces[0] != spaces[1]) and (spaces[0] not in usedSpaces) and (spaces[1] not in usedSpaces):
            ladder_start.append(spaces[0])
            ladder_end.append(spaces[1])
            usedSpaces += spaces
            i += 1
        else:
            i = i

def snake_or_ladders(pos, snake_start, snake_end, ladder_start, ladder_end):
    finalPos = pos

    # Snakes
    for i in range(0, len(snake_start)):
        if pos == snake_start[i]: 
            finalPos = snake_end[i]
            obstacle = "Snake!"
    
    # Ladders
    for i in range(0, len(ladder_start)):
        if pos == ladder_start[i]:
            finalPos = ladder_end[i]
            obstacle = "Obstacle!"
    else: obstacle = "None"
    
    return finalPos, obstacle

def take_turn(startPos, snake_start, snake_end, ladder_start, ladder_end):
    dieRoll = randint(1,6)
    finalPos = startPos + dieRoll
    
    if finalPos > 64: finalPos = startPos

    finalPos, obstacle = snake_or_ladders(finalPos, snake_start, snake_end, ladder_start, ladder_end)
    
    return finalPos, obstacle, dieRoll  


create_board(snake_start, snake_end, ladder_start, ladder_end)

print(f"{len(snake_start)} snakes")
print(f"{len(ladder_start)} ladders")

i = 0
while i < (len(snake_start)):
    print(f"Snake #{i+1}: {snake_start[i]} to {snake_end[i]}")
    i += 1

i = 0
while i < (len(ladder_start)):
    print(f"Ladder #{i+1}: {ladder_start[i]} to {ladder_end[i]}")
    i += 1

player1 = 1
player2 = 1

while 1 == 1:             # Creating an infinite While loop that terminates only when a player reaches the 64th space.
    # Player 1
    print(f"Player 1 is on space {player1}")
    print(f"Player 2 is on space {player2}")
    
    player1_final, obstacle, dieRoll = take_turn(player1, snake_start, snake_end, ladder_start, ladder_end)

    print(f"Player 1 rolls the die: {dieRoll}")
    if obstacle == "Ladder!" or obstacle == "Snake!": print(f"{obstacle}")
    
    player1 = player1_final
    if player1 == 64: 
        print("Player 1 wins!!!")
        break

    # Player 2
    print(f"Player 1 is on space {player1}")
    print(f"Player 2 is on space {player2}")
    
    player2_final, obstacle, dieRoll = take_turn(player2, snake_start, snake_end, ladder_start, ladder_end)

    print(f"Player 2 rolls the die: {dieRoll}")
    if obstacle == "Ladder!" or obstacle == "Snake!": print(f"{obstacle}")
    
    player2 = player2_final
    if player2 == 64: 
        print("Player 2 wins!!!")
        break

