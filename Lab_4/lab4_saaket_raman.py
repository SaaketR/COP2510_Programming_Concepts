# The code for this project represents my own, independent work. I have neither given nor received help on this assignment from other students.
# Saaket Raman

from random import randint

def snake_or_ladders(pos):
    finalPos = pos
    # Snakes
    if pos == 18: finalPos == 1
    if pos == 25: finalPos == 10
    if pos == 44: finalPos == 26
    if pos == 61: finalPos = 47
    if pos == 18 or pos == 25 or pos == 44 or pos == 61: obstacle = "Snake!"
    # Ladders
    if pos == 3 : finalPos == 13
    if pos == 11: finalPos == 28
    if pos == 30: finalPos == 45
    if pos == 42: finalPos == 59
    if pos == 3 or pos == 11 or pos == 30 or pos == 42: obstacle = "Ladder!"

    else: obstacle = "NONE"

    return finalPos, obstacle

def take_turn(startPos):
    dieRoll = randint(1,6)
    finalPos = startPos + dieRoll
    
    if finalPos > 64: finalPos = startPos

    finalPos, obstacle = snake_or_ladders(finalPos)
    
    return finalPos, obstacle, dieRoll

player1 = 1
player2 = 1

while 1 == 1:             # Creating an infinite While loop that terminates only when a player reaches the 64th space.
    # Player 1
    print(f"Player 1 is on space {player1}")
    print(f"Player 2 is on space {player2}")
    
    player1_final, obstacle, dieRoll = take_turn(player1)

    print(f"Player 1 rolls the die: {dieRoll}")
    if obstacle == "Ladder!" or obstacle == "Snake!": print(f"{obstacle}")
    
    player1 = player1_final
    if player1 == 64: 
        print("Player 1 wins!!!")
        break

    # Player 2
    print(f"Player 1 is on space {player1}")
    print(f"Player 2 is on space {player2}")
    
    player2_final, obstacle, dieRoll = take_turn(player2)

    print(f"Player 2 rolls the die: {dieRoll}")
    if obstacle == "Ladder!" or obstacle == "Snake!": print(f"{obstacle}")
    
    player2 = player2_final
    if player2 == 64: 
        print("Player 2 wins!!!")
        break

