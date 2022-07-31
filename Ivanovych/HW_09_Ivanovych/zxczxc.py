def calculator(arg):

    while True:
        try:
            namber1 = int(input('Enter first number: '))
            namber2 = int(input('Enter second number: '))
        except ValueError:
            print("It's not int")
        else:
            break

    def summ(namber1, namber2):
        print(namber1 + namber2)

    def subtrace(namber1, namber2):
        print(namber1 - namber2)

    def multiply(namber1, namber2):
        print(namber1 * namber2)

    def divide(namber1, namber2):
        try:
            print(namber1 / namber2)
        except ZeroDivisionError:
            print('Division by zero')

    if arg == 1:
        return summ(namber1, namber2)

    elif arg == 2:
        return subtrace(namber1, namber2)

    elif arg == 3:
        return multiply(namber1, namber2)

    elif arg == 4:
        return divide(namber1, namber2)

    else:
        print('Value error')


while True:
    try:
        calculator(int(input('\n 1 - +\n 2 - -\n 3 - *\n 4 - / \nEnter command from 1 to 4: ')))
    except ValueError:
        print("Command not found")
    else:
        break
