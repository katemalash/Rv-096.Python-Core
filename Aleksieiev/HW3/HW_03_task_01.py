'''Aleksieiev Valentyn
30/07/2022 HomeWork#3, Task#1
User enters two numbers: a and b. Swap the values of variables a and b without using the additional variable.
'''
from cheker import variable_check

a, b = variable_check(int)
print(f'Original variables: a = {a}, b = {b}')
a, b = b, a
print(f'Swap variables: a = {a}, b = {b}')
