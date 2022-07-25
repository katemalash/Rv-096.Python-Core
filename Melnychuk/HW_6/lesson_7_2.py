import random


#random_matrix = [[random.randint(0, 100) for _ in range(num_of_numbers)] for _ in range(num_of_numbers)]
#print(random_matrix)
random_list = []
num_of_numbers = int(input('Enter the number of the raws in the matrix: '))
for _ in range(num_of_numbers**2):
    random_list.append(random.randint(0, 100))
random_matrix = []
while random_list != []:
    random_matrix.append(random_list[:num_of_numbers])
    random_list = random_list[num_of_numbers:]

for raw in random_matrix:
    print(*raw)

sum_raw_list = []
for i in range(num_of_numbers):
    sum_raw = 0
    for j in range(num_of_numbers):
        sum_raw += random_matrix[i][j]
    sum_raw_list.append(sum_raw)
print(f'This is the list of sums of each raw: {sum_raw_list}')

sum_column_list = []
for i in range(num_of_numbers):
    sum_column = 0
    for j in range(num_of_numbers):
        sum_column += random_matrix[j][i]
    sum_column_list.append(sum_column)
print(f'This is the list of sums of each column: {sum_column_list}')

random_matrix.append(sum_column_list)
for k in range(num_of_numbers):
    random_matrix[k].append(sum_raw_list[k])

for raw in random_matrix:
    print(*raw)