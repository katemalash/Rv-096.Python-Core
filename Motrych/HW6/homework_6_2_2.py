from random import randint

matrix_height=3
matrix_width=4 

lst=[[randint(0,10) for i in range(matrix_width)] for j in range(matrix_height)]

print(f"Original matrix {matrix_width}x{matrix_height} elements is")
[print(*line, sep = "\t") for line in lst]

for i,line in enumerate(lst):
    lst[i] += [sum (line)]
print(f"\n Added a colomn with sum of rows")
[print(*line, sep =  "\t") for line in lst]    

lst.append([sum(lst[j][i] for j in range (matrix_height)) for i in range(matrix_width+1)])
print(f"\n Added a row with sum of colomns")
[print(*line, sep =  "\t") for line in lst]