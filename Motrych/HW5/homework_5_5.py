#Given the number P and the number H. The user enters a sequence of 
#numbers. Determine: the sum of those numbers that are less than P; product 
#of numbers greater than H; the number of numbers in the range of values   
#from P to H. When entering a number equal to P or H, stop the calculation and 
#display the result.

P = float(input("Enter P: "))
H = float(input("Enter H: "))
number = float(input("Enter number: "))
sum = 0
product =1
qty = 0
while number != P and number != H:
    if number < P:
        sum+=number
    if number > H:
        product*=number
    if number > P and number < H:
        qty += 1
    number = float(input("Enter next number: "))    
else:
    print (f"sum is {sum},\nproduct is {product},\nnumber of numbers is {qty}")

