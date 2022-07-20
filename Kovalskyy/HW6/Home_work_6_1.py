from random import randint


rand_list = []
for x in range(0,5):
    n = randint(0,50)
    rand_list.append(n)

user_list =[]
while len(user_list) != 5:
    user_list.append(int(input("Enter numbers: ")))

result = []
for i in range(0,5):
    index_adding = rand_list[i] + user_list[i]
    result.append(index_adding)

print(f"Random list - {rand_list}")
print(f"User list - {user_list}")
print(f"Sum list - {result}")
