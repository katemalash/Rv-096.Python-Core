# The user makes a deposit of n dollars for year at 10% 
# per annum (each year the amount of his deposit increases by 10%. 
# This money is added to the deposit amount, and next year there will also be interest on it).

# Create a bank function that takes the arguments n and years
# and returns the amount that will be in the user's account.

def deposit(n, year):
    amount = n * ((1 + 0.1)**year)
    return amount

print("deposit = %.2f" %deposit(1000,10))
