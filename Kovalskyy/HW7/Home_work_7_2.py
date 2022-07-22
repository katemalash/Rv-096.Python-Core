some_string1 = input("Input a string: ")
some_string2 = input("Input a string: ")

some_string1 = "".join(set(some_string1.lower()))
some_string1 = set(some_string1)
print(f"Alphabetical order of letters that are in first array are:\n{sorted(some_string1)}")

some_string2 = "".join(set(some_string2.lower()))
some_string2 = set(some_string2)
print(f"Alphabetical order of letters that are in second array are:\n{sorted(some_string2)}")

inter_string = some_string1.intersection(some_string2)
print(f"Alphabetical order of letters that are in both arrays are:\n{sorted(inter_string)}")
