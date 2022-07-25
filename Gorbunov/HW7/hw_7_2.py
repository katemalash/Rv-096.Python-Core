first_str = ' A DIMA like Beer. 3 liters a day wW //***=='
second_str = ' Dima hate water. A 3 W glass*/='

char_in_two_lists = sorted(set(first_str).intersection(set(second_str)))
#print(char_in_two_lists)
leters_of_both = [x for x in char_in_two_lists if x.isalpha()] #поверт ліст а треба сет.Але сортед теж повертає ліст
leters_of_first = sorted([x for x in set(first_str) if x.isalpha()])
leters_of_second = sorted([x for x in set(second_str) if x.isalpha()])

print(leters_of_both) # return in alphabetical order the set of leter that are in both arrays
print(leters_of_first)
print(leters_of_second)