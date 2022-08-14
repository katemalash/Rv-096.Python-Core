class Pond:
    """Init the pond. Name is requared. Default: capacity=0, state="poor" """
    def __init__(self, name, capacity=0, state="poor"):
        self.name = name
        self.capacity = capacity 
        self.state=state

    def pond_state (capacity):
        """check the status of pond: poor,normal,rich"""
        if capacity<=5:
            state = 'poor'
        elif 5<=capacity<10:
            state = 'normal'
        else:
            state='rich'
        return state

    def full_info_pond():   # не могу избавиться от None
        """Print full info of the pond"""
        if my_pond.capacity==0:
            print(f"State of pond is {Pond.pond_state(my_pond.capacity)}. Actualy it's empty.")
        else:
            print(f"State of pond is {Pond.pond_state(my_pond.capacity)}. Total weiht of {my_pond.capacity} fishes in {Pond.name} is around {round(Fish.real_fish_weiht_in_pond,2)} kg.")
            print(Fish.fish_in_pond_list)
          

class Fish():
    count=0
    total_weiht=0
    fish_created_type_list =[]
    fish_in_pond_list =[]
    comunity ={}
    real_fish_weiht_in_pond =0
    user_result=0
    
    def __init__(self, type, weiht):
        """Fish initialization. parametr Type and weiht."""
        self.weiht = weiht
        self.type = type
        Fish.count+=1
        Fish.total_weiht+=weiht
        Fish.fish_created_type_list.append(type)
        print(f"Fish '{type}' is born with {weiht} kg. Total {Fish.count} ready to live in a pond.")

    def create_a_fish():
        new_fish=Fish(input("Create fish. Fish type: "),float(input("Create fish. Fish weiht, kg: ")))
        return new_fish

    def add_fish_to_pond():   #!!
        if len(Fish.fish_created_type_list)>0:
            my_pond.capacity+=Fish.count
            Fish.fish_in_pond_list.extend(Fish.fish_created_type_list)   #!!
            Fish.real_fish_weiht_in_pond += Fish.total_weiht
            Fish.total_weiht=0
            Fish.count=0
            Fish.fish_created_type_list.clear()
            print("Created fishes added to Pond")
        else:
            print("No one fish created!")
        #print(Fish.fish_in_pond_list) 
        #print(Fish.fish_created_type_list) 
        return my_pond.capacity
    
    def catch_fish(type, weith):
        if Fish.fish_in_pond_list.count(type)>0:     
            Fish.fish_in_pond_list.remove(type)
            Fish.real_fish_weiht_in_pond= round(Fish.real_fish_weiht_in_pond -weith,2)
            my_pond.capacity-=1
            Fish.user_result+=1
            return print(f"Wow, '{type}', {weith} kg. Good job!")
        else:
            print(f"It is impossible. There is no any '{type}' in a pond.")
    
    def comunity_dict():   #не работает при вылове рыбы. Отображает ее в списке рыб в пруду  (
        # Список проверяется словарем каждый раз в момент его инициализации на этапе добавления в пруд.
        # при ловле рыбы - не хочет менять словарь. Возвращает последнее инициализированное значение.
        for i in Fish.fish_in_pond_list:
            Fish.comunity[i] = Fish.fish_in_pond_list.count(i)   
        print(f"{Pond.name} community is {Fish.comunity}")
        
class UserMenu():
    """Description of user action possibility"""
    def __init__(self,num):
        self.num = num

    def user_input(self):
        print("       ---MENU---")
            
    def menu_logic(num):
        num =int(input("1. Create | 2. Add to pond | 3. Catch | 4. How many fish in a pond | 5. Full pond info | 6. Result | 7. Finish game"))
        while True:
            if num ==1:
                Fish.create_a_fish()
                num =int(input(""))
            elif num==2:
                Fish.add_fish_to_pond()
                num =int(input(""))
            elif num==3:
                Fish.catch_fish(input("Show fish. Fish type: "),float(input("Show fish. Fish weiht: ")))
                num =int(input(""))
            elif num ==5:
                print(f"It is {my_pond.capacity} fish in a pond.")
                num =int(input(""))
            elif num==4:
                print(Pond.full_info_pond())
                num =int(input(""))
            elif num==6:
                print(f"Your curency result is {Fish.user_result} fishes.")
                num =int(input(""))
            else:
                num ==7
                print(f"Total score: {Fish.user_result} fishes. Try again)")
                print(f"--GAME OVER--")
                break
                         
    
my_pond = Pond("Pond without name")
Pond.name="OZERO"

UserMenu.user_input(0)
UserMenu.menu_logic(0)

"""
print(Fish.fish_in_pond_list)            #список верный, а словарь генетирся без изменений
Fish.comunity_dict()
"""

