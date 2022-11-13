# The code for this project represents my own, independent work. I have neither given nor received help on this assignment from other students.
# Saaket Raman

from math import floor

cont1 = float(input("What is the first contestant’s bid? "))
cont2 = float(input("What is the second contestant’s bid? "))
cont3 = float(input("What is the third contestant’s bid? "))
cont4 = float(input("What is the fourth contestant’s bid? "))
truePrice = round(float(input("What is the true price of the bid? ")))

if floor(cont1) < cont1 or floor(cont2) < cont2 or floor(cont3) < cont3 or floor(cont4) < cont4:
    print("Please bid in whole number of dollars!")
else:
    # Setting all overbidded prices to 0 so they do not interfere with comparison of bids:
    if cont1 > truePrice: cont1 = 0
    if cont2 > truePrice: cont2 = 0
    if cont3 > truePrice: cont3 = 0
    if cont4 > truePrice: cont4 = 0

    # Calculating the distance of each bid from the true price. Smallest distance wins. Overbidded prices will always yield the largest distance, hence do not interfere with comparison.
    dist_cont1 = truePrice - cont1
    dist_cont2 = truePrice - cont2
    dist_cont3 = truePrice - cont3
    dist_cont4 = truePrice - cont4

    if cont1 == 0 and cont2 == 0 and cont3 == 0 and cont4 == 0:                                 # Overbidding
        print("All contestants have overbid!")
    else:
        if dist_cont1 < dist_cont2 and dist_cont1 < dist_cont3 and dist_cont1 < dist_cont4:     # Contestant 1
            print("Contestant 1 wins!")
        if dist_cont2 < dist_cont1 and dist_cont2 < dist_cont3 and dist_cont2 < dist_cont4:     # Contestant 2
            print("Contestant 2 wins!")
        if dist_cont3 < dist_cont1 and dist_cont3 < dist_cont2 and dist_cont3 < dist_cont4:     # Contestant 3
            print("Contestant 3 wins!")
        if dist_cont4 < dist_cont1 and dist_cont4 < dist_cont2 and dist_cont4 < dist_cont3:     # Contestant 4
            print("Contestant 4 wins!")

