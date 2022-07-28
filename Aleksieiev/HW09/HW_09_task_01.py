'''Aleksieiev Valentyn
28/07/2022 HomeWork#8, Task#1
Create a function calculator(arg) that takes 1 argument: 1, 2, 3 or 4.
This function should return function sum(a,b) if arg = 1,
dif(a,b) if arg = 2,
product(a,b) if arg = 3 and fraction(a,b) if arg=4.'''
from fractions import Fraction
from operator import add, sub, mul
from cheker import variable_check


MES = '''Input integer number of function to calculate:
1 - sum(a,b)
2 - dif(a,b)
3 - product(a,b)
4 - fraction(a,b)'''
RULES = {1: add, 2: sub, 3: mul, 4: Fraction}

def calculator(arg=1):
    return RULES[arg] if arg in range (1, 5) else None

while True:
    print(MES)  #Print start message
    func = calculator(variable_check(int, 1, 'Input number of function'))
    if func is None:
        print('Your input not valid number!')
        continue
    a, b = variable_check(int, 2, 'Input integer a(#1) & b(#2) to calc the value')
    print(f'a = {a}, b = {b}, function = {func.__name__}, result = {func(a, b)}')
    print('============CALCULATION FINISH============\n')
    if input('Press enter to calculate new deposit or "0" to exit: ') == '0': break

print('Thanks for testing my function bank_function! Have a nice day:)')