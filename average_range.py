"""Write a program to read the numbers until -1 is encountered
Find the average of positive numbers and negative numbers entered by the user"""
negative =0
positive =0
zero = 0
print('Enter -1 to exit the program')
while(-1):
    num=int(input('Enter any number :\t'))
    if num == -1:
        break
    elif num==0:
        zero = zero+1
    elif num>0:
        positive =positive+1
    elif num<0:
        negative = negative+1
averagen= sum(range(0,negative))
averagep = sum(range(0,positive))
average1 = averagen/negative
average2 = averagep/positive
print(f'The total negative numbers entered by user is :\t{negative}')
print(f'The total positive numbers entered by user is :\t{positive}')
print(f'The total zeroes entered by the user is :\t{zero}')
print(f'The average of negative numbers is:\t{average1}')
print(f'The average of positive numbers is :\t{average2}')
