"""Write a program to test whether a number entered by the user is negative positive of equavalent to zero"""
num1 = int(input('Enter any number of your choice :\t'))
if num1 == 0:
    print('The Entered number is 0')
elif num1<0:
    print('The Entered number is a negative number')
elif num>0:
    print('The Entered number is a positive number ')
else:
    print('Invalid input ')
    
