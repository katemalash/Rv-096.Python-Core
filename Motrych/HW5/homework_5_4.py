max_w = int(input("Enter width of rectangle: "))
max_h = int(input("Enter height of rectangle: "))
a=0
b=0
for i in range(max_w):
    if a==1 or a==max_w:
        print("*")
        a=a+1 
for row in range(1, max_h + 1):
    for column in range(1, max_w + 1):
        print(1, end='\t')
    print()