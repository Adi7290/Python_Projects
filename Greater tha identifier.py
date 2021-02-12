#Write a program to find larger of two numbers
a = int(input('Enter the value of num1 :\t'))
b = int(input('Enter the value of num2 :\t'))
if a>b:
    print('Num1 is greater then num 2 ')
elif b>a:
    print('Num2 is greater than num1')
elif a==b|b==a:
    print('Both the values are equal')
else:
    print('Wrong input')
    
