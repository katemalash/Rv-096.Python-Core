'''Aleksieiev Valentyn
04/07/2022 HomeWork#4, Task#3
The user enters a number, the program must display its description. For example, "positive one-digit", "negative two-digit", etc.
'''
from cheker import variable_check

d = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight'}

def count_digids(num):
    return len(str(num).strip('-'))

def pos_neg(num):
    return ('negative', 'positive')[num >= 0]

number = variable_check(int, 1, 'Input your number in')

s = ''
if abs(number) > 9:
    s = 's'
    
print(f'Your number is {pos_neg(number)} {d.get(count_digids(number), "more than eight")}-digit{s}')
    

    