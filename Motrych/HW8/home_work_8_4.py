#  to check: simple or otherwise digits

#def check_simple(a):

a = 139
count = 0 
i = 2
while i <= a:

    if a%i == 0:
        count += 1 
    i += 1
print (count)
if count >= 2:
    print("Number is otherwise")
else:
    print("Number is simple")
 

