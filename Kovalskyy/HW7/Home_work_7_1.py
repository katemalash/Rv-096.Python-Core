some_string = input("Input a string: ")
ulist = []
previous = None
for char in some_string:
    if previous != char:
        ulist.append(char)
        previous=char
print("".join(ulist))
#for char in some_string:
#    if char not in ulist:
#        ulist.append(char)
#print("".join(ulist))
