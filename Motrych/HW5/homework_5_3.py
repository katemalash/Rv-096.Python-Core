max_ = int(input("Enter number from 1 to 9: "))
for row in range(1, max_ + 1):
    for column in range(1, max_ + 1):
        print(row * column, end='\t')
    print()