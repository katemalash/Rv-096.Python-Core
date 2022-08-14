def operation (digit_one, digit_two, arg):
    if arg == "-":
        result = digit_one-digit_two
    elif arg =='+':
        result = digit_one+digit_two
    elif arg =='*':
        result = digit_one*digit_two
    elif arg =='/':
        result = round(digit_one/digit_two, 2)
    else: return("Ubknown operator")
    return(result)

print(operation(50,7,"/"))   


