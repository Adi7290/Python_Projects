"""Write a program that prompts the user to enter a number between 1 and 7 then return the corresponding day according to the users input"""
user_input = int(input('Enter any number from the range of 1-7:\t'))
if user_input == 1:
    print(f"{user_input} is the corresponding day for Sunday")
elif user_input == 2:
    print(f"{user_input} is the corresponding day for Monday")
elif user_input == 3:
    print(f"{user_input} is the corresponding day for Tuesday")
elif user_input == 4:
    print(f"{user_input} is the corresponding day for Wednesday")
elif user_input == 5:
    print(f"{user_input} is the corresponding day for Thursday")
elif user_input == 6:
    print(f"{user_input} is the corresponding day for Friday")
elif user_input == 7:
    print(f"{user_input} is the corresponding day for saturday")
else:
    print('Wrong input')
