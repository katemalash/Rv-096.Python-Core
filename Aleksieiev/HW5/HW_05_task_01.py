'''Aleksieiev Valentyn
12/07/2022 HomeWork#5, Task#1
The program generates a random integer from 0 to 100. The user must guess it in no more than 10 attempts.
After each unsuccessful attempt, program says if the number entered by user more or less than required number.
If the number is not guessed for 10 attempts, then display the guessed number
'''
from cheker import variable_check
from random import randint


check_num = 1
number = randint(0, 100)
answer = 'Your number is '

while check_num < 11:
    user_num = variable_check(int, 1, f"Guess random number from 0 to 100, it's your {check_num} try: ")
    if user_num == number:
        print(f'Congratulations!!! You guessed the number on the {check_num} try!')
        break
    print((answer + 'less', answer + 'more')[user_num > number])
    check_num += 1
else:
    print('Unfortunately you did not guess the number in 10 attempts.')
