multiplicated_numbers = [0,1,2,3,4,5,6,7,8,9]
for i in multiplicated_numbers:
    multiplication = []
    for j in multiplicated_numbers:
        mult = i * j
        multiplication.append(f'{i} * {j} = {mult}')
    print(*multiplication, sep='     ')