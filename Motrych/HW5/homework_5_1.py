secret_number = int(input("Enter secret number from 0 to 100: "))
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
    elif user_number < secret_number:
        print ("The secret number is bigger")
        user_number = int(input("Enter number from 0 to 100: "))   
    print (f"You lost, the secret number is {secret_number}")
       