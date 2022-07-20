from string import printable


char_tuple = tuple(ch for ch in printable)
print(char_tuple)

index = input("\nInput a number, letter or special character to find the index or '0' to exit: ")
while index != '0':
    if index in char_tuple:
        print(f'The index of {index} is: {char_tuple.index(index)}')
    else:
        print('No such number, letter or special character in the tuple')
    index = input('Input 1 number, english letter or special character to find the index or "0" to exit: ')
