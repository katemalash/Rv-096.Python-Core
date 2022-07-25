some_tuple = (1, "a", [6,"q",7], 2,"b", [8,"w",9], 3, "c", [10,"e",11], 4, "d", 5, "e")
num_tuple = []
str_tuple = []
list_tuple = []

for item in some_tuple:
    if type(item)==int:
        num_tuple.append(item)

    elif type(item)==str:
        str_tuple.append(item)
    elif type(item)==list:
        list_tuple.append(item)

print(f"Some_tuple:{some_tuple}")
print(f"\nNumbers in some_tuple:{tuple(num_tuple)}")
print(f"\nStrings in some_tuple:{tuple(str_tuple)}")
print(f"\nLists in some_tuple:{tuple(list_tuple)}")
