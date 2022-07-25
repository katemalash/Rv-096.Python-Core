import random


symbols = input('Enter the symbols you want to be in this task: ')
number_of_elements = int(input('Enter the number of elements in the tuple: '))
symbol_tuple = tuple((random.choices(symbols, k = number_of_elements)))
print(symbol_tuple)
element_list = list(symbol_tuple)

letters_list = []
numbers_list = []
symbol_list = []
for i in range(number_of_elements):
    if element_list[i].isalpha():
        letters_list.append(element_list[i])
    elif element_list[i].isdigit():
        numbers_list.append(element_list[i])
    else:
        symbol_list.append(element_list[i])

list_of_tuples = []
list_of_tuples.append(tuple((letters_list)))
list_of_tuples.append(tuple((numbers_list)))
list_of_tuples.append(tuple((symbol_list)))
print(tuple((list_of_tuples)))