#simple calculator
#Please re run the file if you wanna do the calculation again


one = (int(input('please enter your first number    ')))
sec = (int(input('please enter your second number   ')))
ops = (input('please enter what you want to do with this numbers +,-,*,/,//,%,**   '))

if ops == '+':
    print(one + sec)
elif ops == '-':
    print(one - sec)
elif ops == '*':
    print(one * sec)
elif ops == '/':
    print(one/sec)
elif ops == '//':
    print(one//sec)
elif ops == '**':
    print(one**sec)
elif ops =='%':
    print(one%sec)
else:
    print("print wrong input please run this file again")
