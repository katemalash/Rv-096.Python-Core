'''Aleksieiev Valentyn
19/07/2022 HomeWork#6, Task#2
Calculate the sums of each row and each column of the matrix.
Complete it with a column that contains the sums of the elements of the rows and a row whose elements
are the sums of the elements of the columns.
'''
from random import randint


WIDTH = 3  #number of columns in the random matrix
HEIGHT = 4  #number of rows in the random matrix

lst = [[randint(0, 9) for i in range(WIDTH)] for j in range(HEIGHT)]
print(f'Original random matrix {WIDTH}x{HEIGHT} elements:')
[print(*line, sep='\t') for line in lst]

for i, line in enumerate(lst):
    lst[i] += [sum(line)]
print(f'\nAdded a column with the sum of all elements of the row:')
[print(*line, sep='\t') for line in lst]

lst.append([sum(lst[j][i] for j in range(HEIGHT)) for i in range(WIDTH+1)])
print(f'\nAdded a row with the sum of all elements of the column:')
[print(*line, sep='\t') for line in lst]