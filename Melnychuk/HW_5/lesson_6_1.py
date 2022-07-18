import random


num = random.randint(0, 100)
#print(num)
counter = 0
max_attempt = 10


while counter < max_attempt:
    user_attempt = int(input("Enter the number between 0 and 100: "))
    if user_attempt > num:
        print("Your number is more than required number.")
    elif user_attempt < num:
        print("Your number is less than required number.")
    else:
        print("Congrats! Your quess is right))")
        exit()
    counter += 1
print(f"You'll be lucky next time. The number was: {num}.")