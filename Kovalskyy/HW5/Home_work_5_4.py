outline = "'"
filler = '*'

x = 0
print(outline*20)
while x<5:
    x+=1
    print(outline + filler*18 + outline)
print(outline*20)
