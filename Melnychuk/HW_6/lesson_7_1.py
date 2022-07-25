import random


number_quantity = 5

random_list = []
for _ in range(number_quantity):
    random_number = random.randint(0, 100)
    random_list.append(random_number)
 
user_choice_list = []
count = number_quantity
for _ in range(number_quantity):
    user_choice_number = int(input(f'Enter {count} number: '))
    count -= 1
    user_choice_list.append(user_choice_number)

sum_list = []
for i in range(number_quantity):
    sum_number = user_choice_list[i] + random_list[i]
    sum_list.append(sum_number)

print(f'Those are random numbers: {random_list}\nThose are numbers from the keyboard: {user_choice_list}\nThose are sums: {sum_list}')