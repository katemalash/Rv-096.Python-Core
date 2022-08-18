a=input("Input a: ")
b=input("Input b: ")
try:
    a = int(a)
    b=int(b)
    c=a/b
except ValueError:
    print("Enter only numbers")
except ZeroDivisionError:
    print("You can`t devide on zero")
else:
    print("Everything is ok")
finally:
    print("Calc is working")
