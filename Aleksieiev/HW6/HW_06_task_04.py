'''Aleksieiev Valentyn
19/07/2022 HomeWork#6, Task#4
Divide the tuple into several ones, each of which contains only numbers, only letters, etc. 
'''


orig_tuple = (5,'Word', 8, ['Big WORD', 7, 12, 84, 'Python'], 234, {512}, (1, 5,'A'), [5], 'byte', {5,7,8,2}, 'world', (1,2,3))
nums_tuple = tuple(item for item in orig_tuple if type(item)==int)
str_tuple = tuple(item for item in orig_tuple if type(item)==str)
lst_tuple = tuple(item for item in orig_tuple if type(item)==list)
set_tuple = tuple(item for item in orig_tuple if type(item)==set)
tuple_tuple = tuple(item for item in orig_tuple if type(item)==tuple)

print(f'Original tuple: {orig_tuple}')
print(f'Numbers from original tuple: {nums_tuple}')
print(f'Strings from original tuple: {str_tuple}')
print(f'Lists from original tuple: {lst_tuple}')
print(f'Sets from original tuple: {set_tuple}')
print(f'Tuples from original tuple: {tuple_tuple}')

