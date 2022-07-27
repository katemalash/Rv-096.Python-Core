str_1 = set(input("Enter 1 str: "))
str_2 = set(input("Enter 2 str: "))

unique1 = str_2.difference(str_1)
unique2 = str_1.difference(str_2)

recurring = str_1.intersection(str_2)

print(sorted(unique1.union(unique2)))
print(recurring)
