"""Write a program to calculate the GCD of two numbers"""
num1 = int(input('Enter any num1 of your choice:\t'))
num2 = int(input('Enter any num2 of your choice:\t'))
if num1>num2:
    dividend = num1
    divisor = num2
else:
    dividend = num2
    divisor = num1
#Here we initiate the while loop
while divisor!=0: #here we are conditionalizing the loop
    remainder = dividend%divisor
    dividend= divisor
    divisor=remainder
print(f'The GCD of {num1} and {num2} is {dividend}')