'''Aleksieiev Valentyn
04/07/2022 HomeWork#4, Task#4
Is it possible to place a round stage with radius R in a square hall of square S
so that there is a passage was at least K from the wall to the stage?
'''
from cheker import variable_check



def calc_passage(side, r, k):
    return ("No it's imposibile", "Yes it's possible")[side - 2 * r >= k]


square, r, k = variable_check(int, 3, 'Input square #1 side, #2 radius and #3 k in')

    
print(f'{calc_passage(square, r, k)}! In square hall {square} with round stage {r},\nyou will have at least {square - 2*r} passage')
    

    