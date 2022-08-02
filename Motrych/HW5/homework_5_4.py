# Display a "rectangle" formed of two types of characters. The outline of the 
# rectangle should consist of one character, and "fill" - of another

a = int(input("Input first side of rectangle more then 2 :"))
b = int(input("Input second side of rectangle more then 2 :"))


if a >= 2 and b >= 2:
    res= [["*" if not i or not j or i == a-1 or j == b-1 else "#" for i in range (a)] for j in range(b)]
    [print(*line) for line in res]
       