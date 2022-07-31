def bank(n):
    deposit = 5
    for _ in range(n):
        deposit += 0.1 * deposit
    return deposit

print(bank(5))

