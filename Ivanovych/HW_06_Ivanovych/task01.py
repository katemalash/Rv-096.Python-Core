#Fill in one list with random numbers, another with numbers entered from the keyboard,
#and write the sums of the corresponding elements of the first two lists in the third one.
#Display the contents of the lists on the screen.

from random import randint


random_list = []
for x in range(0,5):
    n = randint(0,100)
    random_list.append(n)

user_list = []
count = 5
for _ in range(0,5):
    user_num = int(input(f'Enter {count} number: '))
    count -= 1
    user_list.append(user_num)


i = list(map(sum,zip(random_list,user_list)))


print(f"Random list - {random_list}")
print(f"User list - {user_list}")
print(f"Sum list - {i}")
