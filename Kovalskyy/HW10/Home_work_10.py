class Fish:
    def __init__(self,weight=5):
        self.weight = weight

class SheatFish(Fish):
    def __init__(self,whisckerLength=10):
        super().__init__()
        self.whisckerLength = whisckerLength
    def __str__(self):
        return f"The fish is sheatfish, with weight {self.weight} and whiscker length {self.whisckerLength}"

class Carp(Fish):
    def __init__(self,color="Grey"):
        super().__init__()
        self.color = color
    def __str__(self):
        return f"The fish is carp, with weight {self.weight} and color {self.color}"
        
class Pond:
    def __init__(self,capacity=None,*state):
        self.capacity = capacity if capacity else []
        self.state = state

    def showState(self):
        if len(self.capacity) <5:
            self.state = "poor"
        elif 5 <= len(self.capacity) < 10:
            self.state = "normal"
        else:
            self.state = "rich"
        print(f"State of the pond: {self.state}")
        
    def showCapacity(self):
        print(f"Capacity of the pond: {len(self.capacity)}")

    def obtainFish(self,fish):
        self.capacity.append(fish)
        print(f"Fish added to pond.\nThere are {len(self.capacity)} fishes")
    
    def lostFish(self):
        if self.capacity:
            fish = self.capacity.pop()
            print(f"Fish removed from the pond. \nThere are {len(self.capacity)} fishes")
            return fish
        else:
            print("The pond is empty")

pond = Pond()

while True:
    print("\n1. View capacity; \
    \n2. View state of Pond; \
    \n3. Add fish( Carp or SheatFish); \
    \n4. Catch fish (concrete instance); \
    \n5. Create new fish (fill himself the creator) \
    \n6. Finish the game.")
    user_input = int(input("Chose an option: "))
    if user_input == 1:
        pond.showCapacity()
    elif user_input == 2:
        pond.showState()
    elif user_input == 3:
        add_fish = int(input("Add Carp(1) or SheatFish(2): "))
        if add_fish == 1:
            carp = Carp()
            pond.obtainFish(carp)
        elif add_fish == 2:
            sheat_fish = SheatFish()
            pond.obtainFish(sheat_fish)
        else:
            print("Wrong input")

    elif user_input == 4:
        fish = pond.lostFish()
        print(f"You catch: \n{fish}")
    
    elif user_input == 5:
        pass
    else:
        break
    