import random

random_number = random.randint(0, 100)
print("Try to guess the number!\n")
counter = 0

while counter < 11:
    user_input = int(input("Please, try to guess magic number between 0 and 100: "))
    if user_input < 0:
        print("Negative numbers are not allowed here!")
    elif user_input > 100:
        print("Numbers bigger than 100 are not allowed here!")
    elif user_input < random_number:
        print("Your magic number is less then hidden one!")
        counter += 1
        continue
    elif user_input > random_number:
        print("Your magic number is greater than hidden one!")
        counter += 1
        continue
    elif user_input == random_number:
        print("You did it! You guessed the hidden number!")
        break
else:
    print(f"You're out of attempts! The magic number is {random_number}.\n Better luck next time!")

