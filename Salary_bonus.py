"""A company decides to give bomus to all its employees on diwali. A 5% bonus on salary is given to the male and 10% bonus for female workers.
Write a program to enter the salary of the employees and sex of the employee .
if the salary of the employee is less than 10,000, then employees get 2 percent extra bonus on salary.
calculate the bonus that has to be given to the employees and display the salary employee will get"""

gender = input('Enter the gender of the employee :\t')
salary = int(input('Enter the salary of the employee :\t'))
if gender == 'm':
    bonus = 0.05*salary
elif gender == 'f':
    bonus ==0.10*salary
if salary<=10000:
    extrabonus = 0.02*salary
def totalsalary():
    amountpaid = salary+bonus+extrabonus
    print(f'This Months salary : \t {salary}')
    print(f'The Bonus of the employee :\t {bonus+extrabonus}')
    print('************************************')
    print(f'Total amount to be paid :\t{amountpaid}')
totalsalary()
