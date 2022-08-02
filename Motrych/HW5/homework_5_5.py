#number of numbers in range

P = float(input("Enter P: "))
H = float(input("Enter H: "))
number = float(input("Enter number: "))
sum = 0
product =1
qty = 0
while number != P and number != H:
    if number < P:
        sum = sum+number
    if number > H:
        product = product*number
    if number > P and number < H:
        qty = qty+1
    number = float(input("Enter next number: "))    
else:
    print (f"sum is {sum},\nproduct is {product},\nnumber of numbers is {qty}")

