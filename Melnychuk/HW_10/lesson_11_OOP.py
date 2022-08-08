class Pond:
    def __init__(self):
        self.capacity = []
        self.state = 'poor'
    
    def update_state_dec( func):
        def wrapper(self, *args, **kwargs):
            func(self, *args, **kwargs)
            if len(self.capacity) < 5:
                self.state = 'poor'
            elif 10 > len(self.capacity) >= 5:
                self.state = 'normal'
            elif len(self.capacity) > 10:
                self.state = 'rich'
            return self.state
        return wrapper
    
    @update_state_dec
    def obtain_fish(self, fish):
        self.capacity.append(fish)
        return self.capacity
        
    @update_state_dec
    def lost_fish(self, fish):
        self.capacity.remove(fish)
        return self.capacity

    def show_capacity(self):
        print(f'In our pond there are: {self.capacity}')
       # return self.capacity
    
    def show_state(self):
        print(f'The pond is {self.state} right now.')
        #return self.state
    
class Fish:
   def __init__(self, weight):
        self.weight = weight
        
        
class SheatFish(Fish):
    def __init__(self, whisker_lenght=5):
        super().__init__(weight=7)
        self.whisker_lenght = whisker_lenght
        
    def __repr__(self):
        return str(f'Sheat{self.whisker_lenght}Fish')
        
class Carp(Fish):
   def __init__(self, color='silver'):
       super().__init__(weight=5)
       self.color = color
        
   def __repr__(self):
        return str(f'{self.color} Carp')
       
synevyr = Pond()
# nemo = SheatFish(7)
# dory = Carp('red')
# marvin = SheatFish(10)
# neo = Carp('blue')
# trin = Carp('black')
# jevgen_karas = SheatFish(9)

# synevyr.obtain_fish(nemo)
# synevyr.obtain_fish(dory)
# synevyr.show_capacity()
# synevyr.lost_fish(nemo)
# synevyr.show_capacity()


def menu():
   print('1. View capacity.')
   print('2. View state of Pond.') 
   print('3. Add fish(Carp or Sheatfish).') 
   print('4. Catch fish(concrete instance).')
   print('5. Create new fish (fill himself the creator).')
   print('6. Finish the game.') 
   
menu()

user_choice = int(input('Enter the number of the menu: '))

while user_choice != 6:
    if user_choice == 1:
        synevyr.show_capacity()
    elif user_choice == 2:
        synevyr.show_state()
    elif user_choice == 3:
        new_option = (input('Enter what fish you want to add to the pond: carp or sheatfish: ')).lower()
        if new_option == 'carp':
            synevyr.obtain_fish(fish=Carp())
        elif new_option == 'sheatfish':
            synevyr.obtain_fish(fish=SheatFish())
        print('Your fish is in the pond already.')
    elif user_choice == 4:
       print(synevyr.capacity)
       number_for_catch = int(input('Those are fishes we have in the pond. Enter the position(number) of fish you want to catch: '))
       synevyr.lost_fish(synevyr.capacity[number_for_catch-1])
       print('Your caught your fish.')
    elif user_choice == 5:
        option = (input('Enter the species of your fish. What will it be?: ')).lower()
        if option == 'carp':
            fish_color = input(f'Enter the color of the fish: ')
            carp_fish = Carp(fish_color)
            carp_fish.weight = int(input('Enter the weight of your fish: '))
            print(f'You created a {carp_fish}, it weights {carp_fish.weight} kilo')
        elif option == 'sheatfish':
            whisker_lenght = input(f'Enter the lenght of whiskers  of the fish: ')
            sh_fish = SheatFish(whisker_lenght)
            sh_fish.weight = int(input('Enter the weight of your fish: '))
            print(f'You created a {sh_fish} with a whiskers {whisker_lenght}cm lenght and weights {sh_fish.weight} kilo.')
        
    else:  
        print('You entered wrong number.')
        
    print()
    #menu()
    user_choice = int(input('Enter the number of the menu: '))
print('You ended the game, so bye)))')