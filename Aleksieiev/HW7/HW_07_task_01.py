'''Aleksieiev Valentyn
22/07/2022 HomeWork#7, Task#1
Character string is given. Develop a program that removes from this line all repeated occurrences
of numbers and signs of arithmetic operations
'''

test_string = 'Ch2arac1ter st1ring i+s give-3n. De&ve%lo9p a prog73r^am that rem/o*ves from this l^i&ne a*l/l 3repe7at%e9d occ+1ur3re-n2ces'
pattern = '01234567890+-0/*%^&'


def del_repeat_num_operators(txt):
    set_num_oper = set()
    res = ''
    for ch in txt:
        if ch not in pattern:
            res += ch
        elif ch in pattern and ch not in set_num_oper:
            res += ch
            set_num_oper |= set(ch)
    return res

def del_all_num_arith1(txt):
    set_num_oper = set()
    res = ''
    for ch in txt:
        if ch not in pattern:
            res += ch
    return res

#Variant#2 for delete all simbols
def del_all_num_arith2(txt):
    res = filter(lambda x: x not in pattern, txt)  
    return ''.join(list(res))

print(f'The original test string is:\n{test_string}')
print(f'\nFunction №1 leaves only unique numbers and operators (on the first occurrence) result:\n{del_repeat_num_operators(test_string)}\n')
print(f'\nFunction №2 delete all nums & operators:\n{del_all_num_arith2(test_string)}\n')

while True:
    text = input('Input a text where you want to delete numbers and arithmetic operations or 0 to EXIT:\n')
    if text != '0':  
        print(f'\nFunction №1 leaves only unique numbers and operators (on the first occurrence) result:\n{del_repeat_num_operators(text)}\n')
        print(f'\nFunction №2 delete all nums & operators:\n{del_all_num_arith2(text)}\n')
        print('===============================================')
    else: break
    
print('Have a nice day:)')