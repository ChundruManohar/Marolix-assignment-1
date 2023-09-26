#a number as input and prints "Positive"
#  if it's greater than zero, "Negative" 
# if it's less than zero, and "Zero" if it's equal to zero.

number = int(input('Enter a number'))
if number>0:
    print('postive number: ' ,number)
elif number<0:
    print('negitve number: ', number)
else:
    print('zero is equal number ',number)
