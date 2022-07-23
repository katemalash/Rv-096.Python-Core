'''Aleksieiev Valentyn
22/07/2022 HomeWork#7, Task#2
There are two character strings of lowercase and uppercase Latin letters and numbers.
Develop a program that builds and prints in alphabetical order the set of letters that are in both arrays and
the set of letters of the first and second arrays separately.
'''

str1 = 'Yd3a2B90zttmmGG'  #test value
str2 = 'b7Gm9taZ0d8mt'  #test value

while True:
    str1, str2 = input('Input the first string or 0 to Exit: '), input('Input the second string or 0 to Exit: ')
    if str1 == '0' or str2 == '0':
        break
    set1 = set(filter(lambda x: x.isalpha(), str1))
    set2 = set(filter(lambda x: x.isalpha(), str2))
    
    print(f'Set of letters from str1: {str1} =', *set1)
    print(f'Set of letters from str2: {str2} =', *set2)
    print(f'Sorted in alphabetical order set1 union set1 =', *sorted(set1 | set2))
    print(f'Sorted in alphabetical order set1 difference with set2 =', *sorted(set1 - set2))
    print(f'Sorted in alphabetical order set2 difference with set1 =', *sorted(set2 - set1))
    print(f'Sorted in alphabetical order the same letters in set1 and set2 =', *sorted(set1 & set2))
    print(f'Sorted in alphabetical order all letter without the same letters in set1 and set2 =', *sorted(set1 ^ set2))
        