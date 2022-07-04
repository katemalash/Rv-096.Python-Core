'''Aleksieiev Valentyn
04/07/2022 HomeWork#4, Task#6
The number of a place in the reserved carriage is given.
Determine which place it is: top or bottom, compartment or side.
'''
from cheker import variable_check


def calc_place_train(number):
    res = 'in the compartment'
    if number > 36:
        res = ' in the side'        
    if not number % 2:
        return 'Upper place ' + res
    return 'Bottom place ' + res
    
            

num_place = variable_check(int, 1, 'Input your place number in the traine Kharkiv-Rahiv between 1 and 54: ')

    
print(calc_place_train(num_place))
if num_place in [1, 2, 3, 4, 54, 53, 34, 33, 35, 36, 38, 39]:
    print('You are the winner! Your place is near the toilet :)!')
    

    