"""Write a program to find whether the given number is an Armstrong Number or not
Hint:An armstrong number of three digit is an integer such that the sum of the cubes of its digits is equal
to the number itself.For example 371 is the armstrong number since 3**3+7**3+1**3"""

num = int(input('Enter the number to check if its an Armstrong number or not :\t'))
orig = num
sm =0
while num>0:
    sm = sm+(num%10)*(num%10)* (num%10)
    num =num//10
if orig == sm:
    print('Armstrong')
else:
    print('Not Armstrong')

