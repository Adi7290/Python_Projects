"""Write a program to calculate the average of first 10 numbers"""
#Here we declare the values of i and s also we are initializing the loop from here
num1=0
num2=0
#Here we create a while loop to calculate the average and sum of first 10numbers

while num1<=10:  #Here we are giving condition to  the loop 
    num2+=num1 # Here we are giving increment to the statement
    num1+=1
average = num2/10
print(f'The Sum of first 10 numbers is :\t{num2}')
print(f'The Average of first 10 numbers is:\t{average}')
