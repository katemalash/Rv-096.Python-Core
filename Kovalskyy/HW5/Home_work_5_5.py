P = int(input("Enter number P: "))
H = int(input("Enter number H: "))

user_number = []
numb_smaler_P = []
numb_bigger_H = []
result_range = []
numb_bigger_H_result =1

while P!= 0 or H!= 0:

    user_number.append(int(input("Enter numbers: ")))
    
    if user_number[-1] < P:                       # Determine: the sum of those numbers that are less than P; 
        numb_smaler_P.append(user_number[-1])

    if user_number[-1] > H:                       # product of numbers greater than H; 
        numb_bigger_H.append(user_number[-1])

        for n in numb_bigger_H:
            numb_bigger_H_result *= n

    if user_number[-1] in range(P,H):             # the number of numbers in the range of values ​​from P to H. 
        result_range.append(user_number[-1])
    
    if user_number[-1] == P or user_number[-1] == H: # When entering a number equal to P or H, stop the calculation and display the result.
        user_number.pop()
        break

    print(f"The P = {P}, H = {H}, numbers = {sorted(user_number)}")

print(f"Sum all numbers less than P: {sum(numb_smaler_P)}")
print(f"Product of numbers greater than H: {numb_bigger_H_result}")
print(f"The number of numbers in the range of values from {P} to {H}: {len(result_range)}")
