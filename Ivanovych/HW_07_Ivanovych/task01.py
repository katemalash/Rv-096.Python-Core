user_set = set()
user_str = input("Enter: ")
userNotDouble = ""

for i in user_str:
    if i not in user_set:
        user_set.add(i)
        userNotDouble += i
print(user_set)
print(userNotDouble)
