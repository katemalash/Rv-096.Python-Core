def deposit_profit(amount, percent, year):
    balance = amount
    for i in range (1,year+1):
        balance = balance*percent/100+balance
    return balance

print(deposit_profit(200,10,1))