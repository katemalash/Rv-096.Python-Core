set1=("1","3","4","4")
set2=set1*2
print(set2)


set3={"Q","W","E","R","T","Y"}
print(set3)
set3.add("M")
set3.discard("Q")
set3.remove("R")
print(set3)
set3.add("Q")

if "W" in set3:
    print(set3)


set3.clear()
print(set3)


name=["ccwe", "cewce", "cewccew"]
sal={}

salary=sal.fromkeys(name,10000)
print(salary)



first={1:"One", 2:"Two", 3:"Three"}
sec={}
for key in first:
    sec[first[key]]=key
print(sec)






