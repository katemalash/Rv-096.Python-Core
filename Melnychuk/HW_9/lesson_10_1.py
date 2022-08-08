def calculator(arg):
    if arg == 1:
        def func(a, b):
            return (a + b)
    elif arg == 2:
        def func(a, b):
            return (a - b)
    elif arg == 3:
        def func(a, b):
            return (a * b)
    elif arg == 4:
        def func(a, b):
            try:
                return (a / b)
            except ZeroDivisionError:
                return 'How Dare You? Division by zero is illegal in this universe.'
    return func

test = calculator(3)
print(test(21,7))