#Write a program to calculate the area of triangle using herons formula
a= float(input("Enter the first side :\t"))
b= float(input("Enter the second side :\t"))
c= float(input("Enter the third side :\t"))
print(f"Side1 ={a}\t,Side2 = {b}\t,Side3={c}")
s = (a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(f"Semi = {s}, and the area = {area}")
