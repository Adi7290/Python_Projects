"""Write a program to calculate the roots of quadractic equation"""
num1 = int(input('Enter the Value of a :\t'))
num2 = int(input('Enter the Value of b :\t'))
num3 = int(input('Enter the value of c :\t'))
D=(num2*num2)-(4*num1*num3)
deno =2*num1
if D>0:
    root1 = (-b+D**0.5)/deno
    root2 = (-b-D**0.5)/deno
    print(f'The Value of Root1: \t{root1} \t The Value Of Root2 is :\t {root2}')
elif D==0:
    print(f'Equal Roots : Root 1 is {root1} \t Root2 is {root2}')
    root1= -num2/deno
    print(f'Root1 and Root2 is :\t {root1}')
else:
    print('IMAGINARY ROOTS')
