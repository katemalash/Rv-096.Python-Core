from random import randint

random_digital = randint (0,100)
first_try = 0
last_try = 10
attempts_left = 10

while first_try<last_try:
    attempt = int(input(f"Guess the digital in diapasone from 0 to 100. You have {last_try-first_try} attempts: "))
    if attempt == random_digital:
        print(f"You guess in {first_try+1} attempts! It realy was {random_digital}.")
        first_try=last_try
        break
    elif attempt<random_digital:
        print(f"Your guess is smaller then Random digital. {attempts_left-1} attempts left.") 
    elif attempt>random_digital:
        print(f"Your guess is bigger then Random digital. {attempts_left-1} attempts left.")
    attempts_left-=1
    first_try+=1
else: print(f"You missed your chance. It was {random_digital}. Try next day")


