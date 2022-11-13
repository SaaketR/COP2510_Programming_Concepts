# The code for this project represents my own, independent work. I have neither given nor received help on this assignment from other students.
# Saaket Raman

truePrice = int(input("What is the true price of the prize? "))
numContestants = int(input("How many contestants are playing today? "))

winner = 0
winBidd_distance = truePrice
numOverbid = 0

i = 1
while i <= numContestants:
    bid = int(input(f"What is the bid for Contestant {i}? "))
    
    bid_distance = truePrice - bid

    if (0 <= bid_distance <= winBidd_distance):
        winner = i
        winBidd_distance = bid_distance
    
    if bid_distance < 0: numOverbid += 1

    i += 1

if numOverbid == numContestants: print("All contestants have overbid!")
else: print(f"Contestant {winner} wins!")
