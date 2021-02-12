"""Write a program to find whether a year is leap year or not """
year = int(input('Enter any year of choice :\t'))
if year%4==0 and year%100!=0 or year%400--0:
    print(f'Entered year {year} is a leap year')
else:
    print(f'Entered year {year} is not a leap year')
