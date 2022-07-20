from random import randint


n = randint(0, 100)
i = 0
while True:
    a = int(input(f"Attempt {i+1}  Enter number: "))
    if a == n:
        print('You win!')
        break
    if a < n:
        print('Hidden number is more')
    else:
        print('Hidden number is less')
    i += 1
    if i == 10:
        print(f'You lost. Hidden number {n}')
        break
