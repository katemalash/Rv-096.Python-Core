def is_prime(number):
    if (number == 2 or number == 3) or (number > 3 and (number**2 - 1) % 24 == 0):
        return True
    else: return False
    
print(is_prime(101))
