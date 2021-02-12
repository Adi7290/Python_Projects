"""program that prompts the user to enter a number and then print its interval"""
num1 = int(input('Enter any number from the range of 0-30:\t'))
if num1>=0 and num1<10:
    print('It is in the range of 0 to 10')
elif num1>=10 and num1<20:
    print('It is in the range of 10 to 20')
elif num1>=20 and num1<30:
    print('Its in the range of 20 to 30')
else:
    print('The number entered is either invalid or is greater than 30')
    
