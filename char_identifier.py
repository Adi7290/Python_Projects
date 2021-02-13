"""Write a program to take the input from the user and then check whether it is a number or a upper lower alphabet"""
char = input('Press Any Key:\t')
if char.isdigit():
    print('The User has entered a Digit')
elif char.isupper():
    print('The user has entered a uppercase letter ')
elif char.islower():
    print('The user has entered a lowercase letter')
else:
    print('Wrong input')
