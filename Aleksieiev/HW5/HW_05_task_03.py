'''Aleksieiev Valentyn
12/07/2022 HomeWork#5, Task#3
Display a multiplication table (1 to 9).
'''
print('The multiplication table from 1 to 9:')
[[print(f'{i} * {num} = {num * i}')for num in range(1, 10)] for i in range(1, 10)]
    