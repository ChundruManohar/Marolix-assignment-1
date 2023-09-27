# Write a Python program that converts a temperature from Celsius to Fahrenheit or vice versa. 
 #Ask the user for the input temperature and a choice of conversion.
 #If the choice is "C to F," convert to Fahrenheit,
 #and if it's "F to C," convert to Celsius.

temp =float(input("Enter Temparature "))
convert = input('convert ')
if convert == 'C to F':
    print(temp*9/5+32)
elif convert == 'F to C':
    print((temp+32)*5/9)
