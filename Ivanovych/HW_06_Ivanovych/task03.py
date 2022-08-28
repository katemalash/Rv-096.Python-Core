'''from random import randint


random_list = []
for x in range(0,5):
    n = randint(0,100)
    random_list.append(n)
print(f"Random list - {random_list}")


for i in random_list(3):
 for j in random_list(3):
     print(random_list[i][j],end='\t')
 print()'''
matrix=[[23,56,10],[59,74,65],[65,23,9]]
minList=[]
minCol=[]

for i in range(3):
    for j in range(3):
     minNum=matrix[j][i]
     minList.append(minNum)
     minColnum=min(minList)
     minCol.append(minColnum)
     minList=[]

minMax=max(minCol)

print(minMax)
'''import random


num_of_numbers = int(input('Enter the number of elements in the raw of the matrix: '))
random_matrix = [[random.randint(0, 100) for _ in range(num_of_numbers)] for _ in range(num_of_numbers)]
for raw in random_matrix:
    print(*raw)

min_numbers_list = []
for j in range(num_of_numbers):
    column_list = []
    for k in range(num_of_numbers):
        column_list.append(random_matrix[k][j])
    #print(column_list)
    min_numbers_list.append(min(column_list))

print(f'Here are minimum elements of the columns {min_numbers_list}\nThe maximum element among the minimum elements of the matrix columns is {max(min_numbers_list)}')'''
