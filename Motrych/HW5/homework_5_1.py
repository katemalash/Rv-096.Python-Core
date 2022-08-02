from random import randint   


secret_number = randint(1,100)
user_number = int(input("Enter number from 0 to 100: "))

if user_number < 0 or user_number > 100:
    user_number = int(input("Enter correct number from 0 to 100: ")) 

for attempt in range (9):
    if user_number == secret_number:
        print (f"You win,the secret number is {secret_number}")
        break
    elif user_number > secret_number:
        print ("The secret number is smaller")
        user_number = int(input("Enter number from 0 to 100: "))
        continue
    elif user_number < secret_number:
        print ("The secret number is bigger")
        user_number = int(input("Enter number from 0 to 100: "))
        continue   
    
print (f"You lost, the secret number is {secret_number}")
       