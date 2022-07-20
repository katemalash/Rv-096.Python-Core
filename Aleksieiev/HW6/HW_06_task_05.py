'''Aleksieiev Valentyn
19/07/2022 HomeWork#6, Task#5
Enter a number, letter or special character from the keyboard and return the entry index to the corresponding tuple accordingly.
'''
from string import printable


big_tuple = tuple(ch for ch in printable[:-5] + '™¡£¢∞§¶•ªº–`œ∑´®†¥¨ˆøπ“‘åß∂ƒ©˙∆˚¬…Ω≈ç√∫˜µ≤≥÷æ«')
print('Big tuple to find the index:', *big_tuple, end='')

find_ch = input('\nInput 1 number, english letter or special character to find the index or "0" to exit: ')
while find_ch != '0':
    if find_ch in big_tuple:
        print(f'The index of {find_ch} is: {big_tuple.index(find_ch)}')
    else:
        print('No such number, letter or special character in the tuple')
    find_ch = input('Input 1 number, english letter or special character to find the index or "0" to exit: ')

else:
    print('Have a nice day:)!')

