"""Write a program to sum the series 1+1/2+....1/n"""
number = int(input('Enter the number :\t'))
sum1=0
for i in range(1,number+1):
    a = 1.0/i
    sum1=sum1+a
print(f'The sum of 1+1/2...1n is {sum1}')