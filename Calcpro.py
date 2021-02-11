user_input = input('Do you want type conversion y or n : \t')
if user_input == 'n':
    #Without convertinig the datatype of input numbers
    a = input('Enter the first Number:')
    b = input('Enter the second Number:')
    print(a+b)
elif user_input == 'y':
    #Using int conversion for datatype conversion
    x= int(input('Enter the first Number'))
    y= int(input('Enter the second Number'))
    print(x+y)
else:
    print('Wrong input')
    
