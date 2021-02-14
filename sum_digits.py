"""Write a program to enter a number and then calculate the sum of its digits"""
sumofdigits =0
number = int(input('Enter a number please :\t'))
while number!=0:
    sums = number%10
    sumofdigits = sums+sumofdigits
    number=number/10
print(f'The sum of the entered number {number} is {int(sumofdigits)}')