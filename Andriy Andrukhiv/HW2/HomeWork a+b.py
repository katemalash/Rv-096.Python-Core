lock = 1

while lock:
    a = int (input('Enter A:'))
    symbol = input ('Press symbol (+, -, *, /):')
    b = int (input('Enter B:'))
    if symbol == '+':
        print (a+b)
    elif symbol == '-':
        print (a-b)
    elif symbol == '*':
        print (a*b)
    elif symbol == '/':
        print (a/b)
    else:
        print('wrong input')
    lock = int(input('Continue? 1 - yes , 0 - no:'))

print('bye')