#Find the maximum element among the minimum elements of the matrix columns
import random


rand_mat_size=int(input("Enter matrix size: "))

random_matrix=[[random.randint(1,100) for i in range(rand_mat_size)] for j in range(rand_mat_size)]
for raw in random_matrix:
    print(*raw)

min_list=[]

for j in range(rand_mat_size):
    colomn_list=[]
    for i in range(rand_mat_size):
        colomn_list.append(random_matrix[i][j])
    min_list.append(min(colomn_list))
print(min_list)        
print(f"The list of minimum elements of matrix colomns is {min_list}\nThe maximim element  among minimum elements of matrix colomns is {max(min_list)}")