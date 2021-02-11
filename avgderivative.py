#Write a program to calculate the average of two numbers and print their derivation
num1 = int(input("Enter the first number :\t"))
num2 = int(input("Enter the second number : \t"))
average = (num1+num2)/2
div1 = num1-average
div2 = num2-average
print(f"The average of the two numbers are {average}\nThe derivation of the first num is {div1}\nThe derivation of the second num is {div2}")
