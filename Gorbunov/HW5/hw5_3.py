a= 9
b= 9
for i in range(1, a+1):
    for j in range(1, b+1):
        if j ==9:
            print(f"{i} * {j} = {i * j}\n", end="\n")
        else: print(f"{i} * {j} = {i * j}\t", end=" ")
             