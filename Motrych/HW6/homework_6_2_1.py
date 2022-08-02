   # add number to matrix  numpy
import numpy


matrix_size = int(input("Enter matrix size: "))
matrix1 = numpy.random.randint(0,100, size=(matrix_size,matrix_size))
print(matrix1)



for i in range(matrix_size):
   sum1=sum(matrix1[i])
   print(f"The sum of{i} row is {sum1} ") 
   sum2=sum(matrix1[:,i])  
   print(f"The sum of{i} colomn is {sum2} ")


print(sum1)
print(sum2)

