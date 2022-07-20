import numpy as np
 

user_choice = int(input("Enter size of a matrix: "))
ran_matrix = np.random.randint(0,50, size=(user_choice, user_choice))
print(f"Random matrix is:\n{ran_matrix}")

count = 0
while count != user_choice:
    count+=1

print(f"The minimum element among the elements of the matrix columns are:\
    \n{np.min(ran_matrix, axis=0)}")
max_el = max(np.min(ran_matrix, axis=0))
print(f"The maximum element among the minimum elements of the matrix colums is:\n{max_el}")
