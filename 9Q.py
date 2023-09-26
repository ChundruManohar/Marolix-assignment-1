#Create a Python program that categorizes people into age groups based on the following criteria:
#0-12 years: Child
#13-19 years: Teenager
#20-59 years: Adult
#60+ years: Senior Ask the user for their age and print their age group.

age = int(input('Enter you are age '))

if age<=12:
    print('you are child ')
elif age>=13 and age<=19:
    print('you are teenagar ')
elif age>=20 and age<=59:
    print('you are a adult ')
else:
    print('you are a senior citizen ')
