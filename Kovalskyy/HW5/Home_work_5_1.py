from random import randint


ran_int = randint(0,100)
print("You have 10 attempts to guess the number!")

count = 0
while count <10:
    count +=1
    guess = int(input("Guess a number: "))

    if 0 < guess > 100:
        print("Wrong number! \nGuess a number from 0 to 100!")
        count -=1
        continue

    elif ran_int == guess:
        print("You win in", count, "try")
        break

    elif ran_int < guess:
        print("You guessed too high!")
        print("This is your's", count, "attempt")

    elif ran_int > guess:
        print("You guessed too low!")
        print("This is your's", count, "attempt")

if count >= 10:
    print(f"The number is {ran_int}! Try next time!" )
