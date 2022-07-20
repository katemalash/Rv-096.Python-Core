import numpy as np
 

user_choice = int(input("Enter size of a matrix: "))
ran_matrix = np.random.randint(0,10, size=(user_choice, user_choice))
print(ran_matrix)

add_column =[]
add_row =[]
count = 0
while count != user_choice:
    count+=1
    row_sum = sum(ran_matrix[count-1])            #Calculate the sums of each row 
    print(f"The sum of {count} row - {row_sum}")
    add_column.append(row_sum)
    
    column_sum = sum(ran_matrix[:,count-1])  #Calculate the sums of each  column 
    print(f"The sum of {count} column - {column_sum}")
    add_row.append(column_sum)

ran_matrix = np.insert(ran_matrix, 0, add_column, axis=1) 

#ran_matrix = np.insert(ran_matrix, 0, add_row, axis=0)
#ran_matrix = np.append(ran_matrix, [add_row], axis=0)
print(f"New matrix - \n{ran_matrix}")
