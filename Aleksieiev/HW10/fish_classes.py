class Fish:
    '''SuperClass "Fish"
has 2 atribute = weight - float (g)
                 age - float (from 0.1 to 10 years old)
when change year - we add weight to fish if new age > old
and sub weight if new age<old

and 1 method __str__'''
    def __init__(self, weight=10, age=0.5):
        self.weight = weight
        self._age = age

    def __str__(self):
        name = self.__class__.__name__
        return f'Class "{name}": {self.__dict__}'
    def __repr__(self):
        name = self.__class__.__name__
        return f'Class "{name}": {self.__dict__}'
    @classmethod
    def create_from_data(cls, weight, age):
        if 0.1<=weight<=30 and 0.1<=age<=10:
            return cls(weight, age)
        else: print('Error with weight = {weight}, age = {age}!')

class SheatFish(Fish):
    '''Class "SheatFish" is a subclass from class "Fish"
has 1 atribute = whisckerLength - int (from 5 to 15 cm)
                 length - float (from 1 to 200 cm)
without methods'''
    def __init__(self, whisckerLength, length):
        super().__init__()
        self.length = length
        self.whisckerLength = whisckerLength

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, x):
        coef = x * 2.4  # add or sub new weight
        self.weight = round(self.weight + [-coef, coef][self._age < x], 2)
        self.length = round(self.length + [-coef*1.2, coef*1.2][self._age < x], 2)
        self.whisckerLength = round(self.whisckerLength + [-coef * 1.1, coef * 1.1][self._age < x], 2)
        self._age = x
        print(f'The Fish {self.__class__.__name__} has new weight, whisckerLength, length and age')

class Carp(Fish):
    '''Class "Carp" is a subclass from class "Fish"
has 2 atribute = color - can be [white, red, black, gold]
                 has_children - Bool: True or False
with 1 methods create_children - when new fish was born
    mother fish -5 weight
    color go to black
    has_children = True
'''

    # ‘poor’, ‘normal’, ‘rich’
    # <5       5-10       10+
    def __init__(self, color, has_children=False):
        Fish.__init__(self)
        self.color = color
        self.has_children =  has_children
    def create_children(self):
        self.has_children = True
        self.color = 'Black'
        self.weight -= 5
STATE = ('POOR', 'NORMAL', 'RICH')
STATE_Score = (5, 10, 11)

class Pond:
    def __init__(self, fish_list=None):
        self.capacity = [fish_list, []][fish_list is None]
        self.__state = None
    def __str__(self):
        name = self.__class__.__name__
        lst_fish = list(map(str, enumerate(self.capacity)))
        answer = '\n'.join(lst_fish)
        return f'Class "{name}":\n{answer}'
    def cath_fish(self, index):
        if index >= self.fish_count:
            return f'No fish with index {index}'
        else:
            return f'Fish with index {index} was deleted\n {self.capacity.pop(index)}'

    @property
    def fish_count(self):
        return len(self.capacity)
    @property
    def __state(self):
        return self.state

    @__state.setter
    def __state(self, x):
        if self.fish_count < 5:
            self.state = STATE[0]
        else:
            self.state = STATE[[1,2][self.fish_count>10]]

