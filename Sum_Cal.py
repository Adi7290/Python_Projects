"""Write a program to calculate the sum of numbers from m to n """
m = int(input('Enter the first Number:\t'))
n = int(input('Enter the second number that you want to put in range:\t'))
s = sum(range(m,n))
while m<=n:
    m=m+n
    print(f'The sum of the numbers will be {s}')
    
    
