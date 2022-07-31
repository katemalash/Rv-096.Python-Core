def arithmetic_operations(num_1, num_2, ar_operator):
    operators = ['+', '-', '*', '/']
    if ar_operator not in operators:
        return 'Unknown operation'
    else: 
        result = eval(f'{num_1} {ar_operator} {num_2}')
        return result
  
print(arithmetic_operations(100, 1, '+'))


