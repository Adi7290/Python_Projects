"""Write a program to reverse of a entered number """
num1 = int(input('Enter any number of your choice:\t'))
print('The reversed number is :',)
while num1!=0:
    temp = num1%10
    print(temp,end=" ")
    num1=num1/10