# The code for this project represents my own, independent work. I have neither given nor received help on this assignment from other students.
# Saaket Raman

def load_game(filename):
    game = open(filename, mode = "r")

    numPlayers = int(game.readline())
    currentPlayer = int(game.readline())
    direction = int(game.readline())
    numCardsPerPlayer = dict()
    playerHands = dict()
    playerNames = []

    for a in range(1, numPlayers + 1):
        x = game.readline()
        x = x.strip()
        numCardsPerPlayer[x] = ""
        playerHands[x] = ""
        playerNames.append(x)

    for a in numCardsPerPlayer.keys():
        numCardsPerPlayer[a] = int(game.readline())

    numDiscard = int(game.readline())
    numDeck = int(game.readline())

    for a in playerHands.keys():
        hand = list()
        i = 1
        while i <= numCardsPerPlayer[a]:
            card = game.readline()
            card = card.strip()
            hand.append(card)
            i += 1
        
        for b in range(0,len(hand)):
            hand[b] = full_name(hand[b])
        
        playerHands[a] = hand

    discardedCards = list()
    for a in range(0,numDiscard):
        card = game.readline()
        card = card.strip()
        discardedCards.append(full_name(card))
    
    print(f"Top Card: {discardedCards[0]}")

    print("")

    print("Your hand:")
    for a in playerHands[playerNames[0]]: print(a)

    print("")

    for a in range(1,numPlayers):
        print(f"{playerNames[a]}'s hand: {numCardsPerPlayer[playerNames[a]]} card(s)")


def full_name(card):
    cardName = ""
    
    if card == "WI": cardName = "Wild"
    elif card == "W*": cardName = "Wild Draw Four"
    else:
        color, num_or_eff = card.strip()
        color_Name = ""
        num_or_eff_Name = ""

        if color == "R": color_Name = "Red"
        elif color == "G": color_Name = "Green"
        elif color == "B": color_Name = "Blue"
        elif color == "Y": color_Name = "Yellow"
        
        if num_or_eff == "S": num_or_eff_Name = "Skip"
        elif num_or_eff == "R": num_or_eff_Name = "Reverse"
        elif num_or_eff == "D": num_or_eff_Name = "Draw Two"
        else: num_or_eff_Name = num_or_eff
        cardName = color_Name + " " + num_or_eff_Name

    return cardName


file = input()

load_game(file)

