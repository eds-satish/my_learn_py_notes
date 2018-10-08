
a = int(input('Enter value for a: '))
b = int(input('Enter value for b: '))

op = input('Enter the operator you want +, -, *, /: ')

if op == '+':
    c = a + b
    print('Sum is: ', c)
elif op == '-':
    c = a - b
    print('Sub is: ', c)
elif op == '*':
    c = a * b
    print('Mul is: ', c)
elif op == '/':
    c= a / b
    print('Div is: ', c)
else:
    print('Invalid operator')
    


