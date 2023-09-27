'''Implement a simple menu-driven program in Python.
Ask the user to choose an option from a menu
(e.g., 1 for "Calculate Area," 2 for "Calculate Perimeter," 3 for "Exit")'''

a = int(input('Enter a length : '))
b = int(input('Enter a width : '))

Area = a*b #Area = length * width
import math

Perimeter = 2*(a + b)  #Perimeter of reactangle p = 2(L+W)
print("Total area is: ", Area)
print("Total area of rectangular : ", Perimeter)