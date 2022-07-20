from random import randint


row = int(input("Input number of rows: "))
colum= int(input("Input number of colums: "))

rand_matrix = [[randint(0,10) for a in range(row)] for b in range(colum)]
print(f"The matrix is: \n{rand_matrix}")

for i, line in enumerate(rand_matrix):
    rand_matrix[i] += [sum(line)]
print(f'Added a column with the sum of all elements of the row:')
[print(line, sep='\t') for line in rand_matrix]

rand_matrix.append([sum(rand_matrix[j][i] for j in range(colum)) for i in range(row+1)])
print(f'Added a row with the sum of all elements of the column:')
[print(line, sep='\t') for line in rand_matrix] 
