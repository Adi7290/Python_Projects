'''Write a program to prepare a grocery bill , for that enter the name of items , quantity in which it is
purchased and its price per unit the display the bill in the following format
*************BILL***************
item name    item quantity    item price
********************************
total amount to be paid :
*********************************'''

name = input('Enter the name of item purchased :\t')
quantity = int(input('Enter the quantity of the item :\t'))
amount = int(input('Enter the amount of the item :\t'))
item_price = quantity * amount
print('*****************BILL****************')
print(f'Item Name\t Item Quantity\t Item Price')
print(f'{name}\t\t {quantity}\t\t {item_price}')
print('************************************')
print(f'Price per unit is \t \t {amount}')
print('************************************')
print(f'Total amount :\t\t{item_price}')
print('************************************')
