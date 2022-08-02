#Divide the tuple into several ones, each of which contains only numbers, only letters, etc.

tup1=(1,2,3,True, "qwe")
list_int=[]
list_str=[]
list_bool=[]
for i in range(len(tup1)):
    if (isinstance(tup1[i],int)):
        print(f"{tup1[i]} is int")
        list_int.append(tup1[i])
    else:
        print(f"{tup1[i]} is not int")
    if (isinstance(tup1[i],str)):
        print(f"{tup1[i]} is str")
        list_str.append(tup1[i])
    else:
        print(f"{tup1[i]} is not str")
    if (isinstance(tup1[i],bool)):
        list_bool.append(tup1[i])
        print(f"{tup1[i]} is bool")
    else:
        print(f"{tup1[i]} is not bool")
list_int=(list_int)
list_str=(list_str)
list_bool=(list_bool)

print(list_int)   
print(list_str)
print(list_bool)        
