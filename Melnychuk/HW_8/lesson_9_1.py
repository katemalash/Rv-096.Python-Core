def arithmetic_operations(num_1, num_2, ar_operator):
    if ar_operator == '+':
        return num_1 + num_2
    elif ar_operator == '-':
        return num_1 - num_2
    elif ar_operator == '*':
        return num_1 * num_2
    elif ar_operator == '/':
        return num_1 / num_2
    else: 
        return 'Unknown operation'
  
print(arithmetic_operations(1050, 2, '/'))