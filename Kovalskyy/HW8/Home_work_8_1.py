# Create an arithmetic function that takes 3 arguments: 
# the first 2 are numbers, the third is the operation to be performed on them. 
# If the third argument is +, add them; if -, then subtract; * - multiply;
# / - divide (first to second). 
# In other cases, return the "Unknown operation" line.

def makeOperations(a,b,arg: str):
    if arg == "+":
        return a+b
    elif arg == "-":
        return a-b
    elif arg == "*":
        return a*b
    elif arg == "/":
        return a/b
    else:
        return "Unknown operation"
#print(makeOperations(10,20, "+"))
print(makeOperations(int(input("Input a: ")),int(input("Input b: ")), input("Input arg: ")))
