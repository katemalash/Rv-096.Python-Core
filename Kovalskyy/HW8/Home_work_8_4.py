# Create the function is_prime, which takes 1 argument - a number from 0 to 1000,
# and returns True if it is simple, and False - otherwise. 

def is_prime(num):
    if num >1:
        for i in range(2,num):
            if num%i == 0:
                return False
        else:
            return True
    else:
        return False
    
num = int(input("Input a number from 0 to 1000: "))
print(is_prime(num))
