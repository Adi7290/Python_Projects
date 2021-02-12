"""Write a program to calculate the tax given in the following conditions
if income is less than 1,50,000 then no tax is applicable
if income is 1,50,000- 3,00,000 annual tax will be 10%
if income is 3,00,000-5,00,000 annual tax will be 20%
if income is more then 5,00,000 annual tax will be 30%"""

income = int(input('Enter your annual income please'))
if income <=150000:
    print('No tax is applied on the annual income')
elif income > 150000 and income<300000:
    tax10 = income*0.10
    print(f'The applied tax on the income is 10% so your tax amount will be {tax10}')
elif income > 300000 and income<500000:
    tax20 = income*0.20
    print(f'The applied tax on the income is 20% so your tax amount will be {tax20}')
elif income>500000:
    tax30 = income*0.30
    print(f'The applied tax on the income is 30% so your tax amount will be {tax30}')
