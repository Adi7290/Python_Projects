"""Write a program that identifies that character entered by user is a vowel or not """
ch = input('Enter any Alphabet:\t')
if ch.upper() =='A' or ch.lower() =='E' or ch.lower() =='I' or ch.lower() =='O' or ch.lower() =='U':
    print(f'The entered alphabet {ch} is a vowel')
elif ch.isdigit():
    print(f'The entered character {ch} is a number')
else:
    print(f'Entered character {ch} is a usual alphabet')
    
