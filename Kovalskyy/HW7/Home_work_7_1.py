some_string = input("Input a string: ")

some_string = "".join(sorted(set(some_string)))
print(some_string)
