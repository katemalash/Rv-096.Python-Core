'''Aleksieiev Valentyn
19/07/2022 HomeWork#6, Task#3
Find the maximum element among the minimum elements of the matrix columns. 
'''
from random import randint


WIDTH = 4  #number of columns in the random matrix
HEIGHT = 4  #number of rows in the random matrix

lst = [[randint(0, 25) for i in range(WIDTH)] for j in range(HEIGHT)]
print(f'Original random matrix {WIDTH}x{HEIGHT} elements:')
[print(*line, sep='\t') for line in lst]

min_lst = [min(lst[j][i] for j in range(HEIGHT)) for i in range(WIDTH)]
print('\nMinumum elements of each colums:')
[print(*min_lst, sep='\t')]

print('\nMaximum element among the minimum elements of the matrix columns:')
print(max(min_lst))
