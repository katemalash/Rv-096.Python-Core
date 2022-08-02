# arithmetic function

def combine(x,y,sign):

    if sign == "+":
       res = x+y 
    elif sign == "-": 
       res = x-y 
    elif sign == "/": 
       res = x/y
    elif sign == "*": 
       res = x*y
    else:
        return "Unknown symbol"
    return res

print(combine(30,1,"-"))


        