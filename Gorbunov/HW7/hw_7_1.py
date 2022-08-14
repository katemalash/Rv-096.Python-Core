import itertools


a = "aaabbc a b c  a  b         c"
b = list(a) #(a.replace(" ",""))
c = [i[0] for i in itertools.groupby(b)]
print(b)
print (c)
