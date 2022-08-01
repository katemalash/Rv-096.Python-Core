# Create a function calculator(arg) that takes 1 argument: 1, 2, 3 or 4. 
# This function should return function sum(a,b) if arg = 1, 
# dif(a,b) if arg = 2, product(a,b) if arg = 3 and fraction(a,b) if arg=4.


num = int(input("Enter 1 for sum, 2 for dif, 3 for product, 4 for fraction: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))

def calculator(num):
    def sum(a,b):
        return a+b
    def dif(a,b):
        return a-b
    def product(a,b):
        return a*b
    def fraction(a,b):
        return a/b
    def wrong_input(a,b):
        return "Wrong input"

    if num == 1:
        return sum
    elif num == 2:
        return dif
    elif num == 3:
        return product
    elif num == 4:
        return fraction
    else:
        return wrong_input
        
calc = calculator(num)
print(f"The result is: {calc(a,b)}")

