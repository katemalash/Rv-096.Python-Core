'''Task #1 (Aleksieiev Valentin)
Define variables a and b. Read values a and b from console and calculate: 
a + b, a - b, a * b, a / b. 
   Output obtained results.
'''

a, b = int(input(f'Input variable a: ')), int(input(f'Input variable b: '))
for i in '+-*/':
    print(f'a {i} b = {round(eval(str(a) + i + str(b)), 2)}')
    
# eval is very bad function, but it works in this case very nice:)
# print(f'a + b = {a + b}')
# print(f'a - b = {a - b}')
# print(f'a * b = {a * b}')
# print(f'a / b = {a / b}')
