#exam score (0-100) and prints
#"A" if the score is 90 or above, 
#"B" if it's between 80 and 89,
#"C" if it's between 70 and 79, 
#"D" if it's between 60 and 69, 
#and "F" if it's below 60

d = int(input('Enter your scoure '))
if d>=90 and d<=100:
    grade = "A"
elif d>=80 and d<=89:
    grade ="B"
elif d>=70 and d<=79:
    grade ="C"
elif d>=60 and d<=69:
    grade ="D"
else:
    grade ="F"
print("you are grade ",grade)
