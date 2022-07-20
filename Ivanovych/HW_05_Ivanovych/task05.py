P = 56
H = 95
sum = 0
mult = 1
gap = 0

while True:
    num = int(input('Enter the number: '))

    if num == P or num == H:
        break
    else:
        if num < P:
            sum += num
        elif num > H:
            mult *= num
        else:
            gap += 1

print('Sum of numbers that are less than P: ', sum)
print('Multiplication of numbers that are grater than H: ', mult)
print('Numbers between P and H are: ', gap)
