# Enter a number, letter or special character from the keyboard 
# and return the entry index to the corresponding tuple accordingly


total=tuple("1234567890")
elem=input("Enter element ")
if elem not in total:
    print("not in list")
else:
    index = total.index(elem)
    print(index)