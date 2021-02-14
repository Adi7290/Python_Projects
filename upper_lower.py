"""Write a program to read a character until a * is encountered,
Also calculate the uppercase,lowercase and numbers entered by the user"""
#Here we are declaring empty values so that it can be incremented or decremented
upper = 0
lower = 0
number = 0
res = input('Enter Any character:\t')
if res.isupper():
    upper=upper+1
elif res.islower():
    lower = lower+1
elif res.isdigit():
    number = number+1
#Here we conditionalize the loop and reiterate over our condition
while res != '*':
    res = input('Enter Any character:\t')
    #here we are incrementalizing the value 
    if res.isupper():
        upper=upper+1
    elif res.islower():
        lower = lower+1
    elif res.isdigit():
        number = number+1
print(f'The user has entered {upper} times uppercase letter ')
print(f'The user has entered {lower} times lowercase letter ')
print(f'The user has entered {number} times numeric values ')
