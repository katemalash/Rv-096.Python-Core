#Divide the tuple into several ones, each of which contains only numbers, only letters, etc

diff_things = ('ice', 'u', 25, 48, 11, 44, 'boo', 1.5, 2.25, 9.457)
print(diff_things)

num = []
float_num = []
letters = []

for thing in diff_things:
    if type(thing) == int:
        num.append(thing)
    elif type(thing) == float:
        float_num.append(thing)
    elif type(thing) == str:
        letters.append(thing)

print(num)
print(float_num)
print(letters)
