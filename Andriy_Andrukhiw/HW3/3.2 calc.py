byte = int(input("Press byte: "))
kbyte = byte/1024
mbyte = kbyte/1024
action = input("kbyte or mbyte? (k - m): ")
if action == "k":
    print(kbyte)
elif action == "m":
    print(mbyte)
else:
    print("not entered correctly")