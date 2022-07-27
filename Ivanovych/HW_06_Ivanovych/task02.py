#Calculate the sums of each row and each column of the matrix.
#Complete it with a column that contains the sums of the elements of the rows and
#a row whose elements are the sums of the elements of the columns.

row1=[1,2,3]
row2=[4,5,6]
row3=[7,8,9]
sumRow=[]
matrix=[row1,row2,row3]

print('Input matrix')

for i in range(3):
 for j in range(3):
     print(matrix[i][j],end='\t')
 print()

sumNum1=0
sumNum2=0
sumNum3=0

for i in range(3):
 sumNum1=sumNum1+row1[i]
 sumNum2=sumNum2+row2[i]
 sumNum3=sumNum3+row3[i]
 sumRowNum=row1[i]+row2[i]+row3[i]
 sumRow.append(sumRowNum)

row1.append(sumNum1)
row2.append(sumNum2)
row3.append(sumNum3)
sumRow.append(row1[3]+row2[3]+row3[3])

matrix=[row1,row2,row3,sumRow]

print('Output matrix')

for i in range(4):
 for j in range(4):
     print(matrix[i][j],end='\t')
 print()
