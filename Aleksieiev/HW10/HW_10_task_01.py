'''Aleksieiev Valentyn
02/08/2022 HomeWork#10, Task#1
Fish. It has weight.
Fish has two derived classes: SheatFish and Carp.
SheatFish should have whisckerLength, Carp should have color.
You can also add optional attributes (as you wish).'''

from fish_classes import Fish, Carp, SheatFish

fish = Fish(10)
s_fish = SheatFish(18, 12)

# print(f'Original Fish:\n{fish}\n{s_fish}\n{c_fish}')
print(f'Original SheatFish:\n{s_fish}')
input('         PRES ENTER TO CONTINUE')
print('===============================================')
#SheatFish we change age and wheight changes too
s_fish.age += 2

print(f'Older SheatFish age +2 year:\n{s_fish}')
print('===============================================')
input('         PRES ENTER TO CONTINUE')
#SheatFish we change age and wheight changes too
s_fish.age -= 0.5
print(f'Younger Carp -0.5 year:\n{s_fish}')
print('===============================================')
input('         PRES ENTER TO CONTINUE')
print('===============================================\n\n')
c_fish = Carp(12, 'white')
print(f'Original Carp:\n{c_fish}')
c_fish.create_children()
print('===============================================')
print(f'Carp gave birth to many small fish and lost weight and change color:\n{c_fish}')
# print(f'Original Fish:\n{fish}\n{s_fish}\n{c_fish}')
