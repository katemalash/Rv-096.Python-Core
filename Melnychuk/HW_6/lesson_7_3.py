import random


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

print(f'Here are minimum elements of the columns {min_numbers_list}\nThe maximum element among the minimum elements of the matrix columns is {max(min_numbers_list)}')
