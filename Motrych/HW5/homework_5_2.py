user_number = int(input("Enter number greater then 2: "))
if user_number <= 2:
    user_number = int(input("Enter correct number greater then 2: "))
multi_5 = 0
for i in range(9):   
    user_number = int(input("Enter number greater then 2: "))
    if user_number % 5 == 0:
        multi_5 += 1 
print(f"There are {multi_5+1} numbers that are multiples of 5")        