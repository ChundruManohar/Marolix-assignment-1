#Create a Python program that checks 
#if a given year is a leap year.
#If the year is divisible by 4 but not divisible by 100, or it's divisible by 400, it's a leap year. Otherwise, it's not.

Year  =int(input("Enter a year "))
if Year%400==0:
    print('leap year')
else:
    if Year%4==0 or  Year%100:
        print('leap year')
    else:
        print('Not leap year')
