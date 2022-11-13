# The code for this project represents my own, independent work. I have neither given nor received help on this assignment from other students.
# Saaket Raman

'''
Estimating the area of a circle, given the circumference (C).
    First found radius (r) from the circumference (C = 2 * pi * r)
    Then substituted r into the formula for area of a circle (pi * r^2)
'''

pi = 3.1416
C = 100
r = C / (2 * pi)
area = pi * (r**2)
print(f'{area:.2f}')

print("")

'''
Estimating the area of a flower, given radius of a flower (r).
    Length of side of square is equal to r.
    Radius of semi circle is equal to half the r
    Found area of square using the formula (side)^2
    Found area of semicircle using the formula (pi * r^2)/2
Finally, found the sum of the square's area with four times the area of the semicircle.

'''

pi = 3.1416
r = 4.5
areaSquare = r**2
areaSemi = (pi * (r/2)**2)/2
areaFlower = areaSquare + (4 * areaSemi)
print(f'{areaFlower:.4f}')

print("")

'''
Estimating the area of a flower, using radius inputted by the user.
    Asked for user input, converted input to a float variable.
    Followed the same calculations as previous question.
    
'''

r = float(input("Enter radius of a flower: "))
areaSquare = r**2
areaSemi = (pi * (r/2)**2)/2
areaFlower = areaSquare + (4 * areaSemi)
print(f'{areaFlower:.4f}')

print("")

'''
Caculating the value of loan using the formula P * e^(r*t), where P is Principle, r is interest rate, 
and t is number of years, and e is Euler's Constant.
    P, r, and t are user inputted variables, that are converted to a float variable.
    Value of loan is then calculated and printed.
'''

P = float(input("Enter the principle: "))
r = float(input("Enter the interst rate: "))
t = float(input("Enter time (in years): "))
e = 2.718
value = P * e**(r*t)
print(value)
