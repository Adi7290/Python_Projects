#Write a program to determine the character entered by the user
char = input("Press Any Key : ")
if char.isalpha():
    print('The user has entered a character :\t')
if char.isdigit():
    print('The user has entered a digit : \t ')
if char.isspace():
    print("The user has entered a white space character:\t")
