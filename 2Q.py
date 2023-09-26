#If the age is less than 18, it should print "You are a minor." 
# If the age is between 18 and 65, it should print "You are an adult."
#  If the age is 65 or older, it should print "You are a senior citizen." 

age = int(input("Enter you are age "))
if age<18:
    print('you are a minor: ',age)
elif age>=18 and age<=65:
    print('You are an adult: ',age)
else :
    print('you are a senior citizen ',age)
