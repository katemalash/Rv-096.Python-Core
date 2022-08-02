# Character string is given. Develop a program that removes from this line 
# all repeated occurrences of numbers and signs of arithmetic operations

ls1 = ["q","w","e","r","r","r","r","r","r","t","t","y","u","i","o","o","p"]
ls2 = [ls1[0]]
i = 1
j = 0
while i < len(ls1):
    if ls2[j] != ls1[i]:
        ls2.append(ls1[i]) 
        j += 1 
    i += 1

print (ls2)