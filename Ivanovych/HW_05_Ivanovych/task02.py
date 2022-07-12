
a = int(input("Enter 1 number: "))
b = int(input("Enter 2 number: "))
c = int(input("Enter 3 number: "))
d = int(input("Enter 4 number: "))
e = int(input("Enter 5 number: "))
#print(a,b,c,d,e)
i = 0
for i in (a,b,c,d,e):
    if i % 5 == 0 :
        print("Numbers are multiples of 5:")
        print(i)
