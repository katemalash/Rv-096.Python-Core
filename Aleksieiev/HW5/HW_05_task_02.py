'''Aleksieiev Valentyn
12/07/2022 HomeWork#5, Task#2
User enters ten natural numbers greater than 2. Count how many of them are numbers that are multiples of 5.
'''
from cheker import variable_check


num_lst = variable_check(int, 10, f"Input 10 numbers greater than 2")
mult_lst = list(filter(lambda x: x%5==0, num_lst))
if mult_lst:
    print('Numbers multiples of 5 in your inputs:', end=' ')
    print(*mult_lst, sep=', ')
else:
    print('There are no numbers in your input that are multiples of 5')