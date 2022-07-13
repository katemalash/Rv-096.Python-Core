positive = []
negative = []
user_num = []

while user_num !=0:

    user_num.append(int(input("Enter a number to calc or '0' to finish: ")))

    if user_num[-1] > 0:
        positive.append(user_num[-1])
    elif user_num[-1] < 0:
        negative.append(user_num[-1])

    if user_num[-1] == 0:
        user_num.pop()
        break
    
#print(user_num, positive, negative)
print(f'The positiv numbers are: {len(positive)/len(user_num)*100} percentage')
print(f'The negative numbers are: {len(negative)/len(user_num)*100} percentage')


