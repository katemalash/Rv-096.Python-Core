user_input = input("Enter the text: ").split()

user_dict = dict()

for word in user_input:
    if word in user_dict:
        user_dict[word] += 1
    else:
        user_dict[word] = 1

print(user_dict)
    