'''Aleksieiev Valentyn
12/07/2022 HomeWork#5, Task#5
Given the number P and the number H. The user enters a sequence of numbers.
Determine: the sum of those numbers that are less than P; product of numbers greater than H;
the number of numbers in the range of values ​​from P to H.
When entering a number equal to P or H, stop the calculation and display the result
'''
from cheker import variable_check
from functools import reduce

P, H = variable_check(int, 2, f"Input number P and H to calculate")
num_lst = []
while True:
    try:
        num_lst.append(int(input(f'Input your int number to calc or ({P}, {H}) to finish: ')))
    except Exception:
        print('You input not integer number')
        continue
    
    if num_lst[-1] in [P, H]:
        break
    else:
        print(f'The P = {P}, H = {H}, numbers = {sorted(num_lst)}')

        les_p_sum = sum(filter(lambda x: x<P, num_lst))  # sum all numbers less than P
        if les_p_sum:
            print(f'1. Sum all numbers less than P: {les_p_sum}')
        else:
            print(f'1. There are no numbers less than P')
        
        gre_h_lst = list(filter(lambda x: x>H, num_lst))  # all numbers greater than H
        gre_h_mul = reduce(lambda x, y: x*y, gre_h_lst, 1)  # multuply all numbers greater than H
        if gre_h_lst:
            print(f'2. Multuply all numbers greater than H: {gre_h_mul}')
        else:
            print(f'2. There are no numbers greater than H')

        num_ph_ran = filter(lambda x: x in range(min(P, H)+1, max(P, H)), num_lst)  # the number of numbers in the range of values ​​from P to H.
        if num_ph_ran:
            print(f'3. The number of numbers in the range of values ​​from {P} to {H}: ', end='')
            print(*num_ph_ran, sep=', ')
        else:
            print(f'3. There are no numbers in the range of values ​​from P to H')
        print('===============================================================\n')

print('I hope you liked it :)')


    