'''Write a program to determine whether a person is eligible to vote or not , if user is not eligible for the
vote how  many years he have to wait to be eligible'''

age = int(input("Enter your age :\t"))
if age >=18:
    print('You are eligible for vote')
else:
    years = 18-age
    print(f'Sorry You are not eligible for voting wait for {years} to get eligibility')
