"""Write a program to read the numbers until a -1 is encountered ,
Also count the negative and positive and zeroes entered by the user """
negative = 0
positive = 0
zeroes = 0
print('Enter -1 to exit the program...')
while(-1):
    num=int(input('Enter any number :\t'))
    if num == -1:
        break
    if num == 0:
        zeroes= zeroes+1
    elif num>0:
        positive = positive +1
    else:
        negative=negative+1
print(f'The  total Negative Numbers Entered by user :\t{negative}')
print(f'The Total Positive numbers Entered by user :\t{positive}')
print(f'The Total zeroes Entered by user :\t{zeroes}')
