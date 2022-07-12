'''Aleksieiev Valentyn
12/07/2022 HomeWork#5, Task#4
Display a "rectangle" formed of two types of characters.
The outline of the rectangle should consist of one character, and "fill" - of another.
'''
from cheker import variable_check


a, b = variable_check(int, 2, f"Input 2 sides of the rectangle more then 2")
if a >= 2 and b >= 2:
    res = [['*' if not i or not j or i==a-1 or j==b-1 else '#' for i in range(a)]for j in range(b)]   
    [print(*line) for line in res]
else:
    print('Sorry, you input less then 2')

    
    