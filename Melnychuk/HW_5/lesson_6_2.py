num_quantity = 10
num_number = num_quantity
counter = 0
list_of_nums = []

print(f"You'll have to enter {num_quantity} natural numbers grater than 2.")

while counter < num_quantity:
    user_nums = input(f"Enter the {num_number} natural number: ")
    if not user_nums.isdigit() or int(user_nums) <= 2:
        print(f'Wrong number.Try again.')
    else:
        list_of_nums.append(int(user_nums))
        counter += 1
        num_number -= 1
#print(list_of_nums)

sum = 0
for i in list_of_nums:
    if i % 5 == 0:
        sum +=1
print(f'You entered {sum} numbers that are multiplies of 5')


