#I have used someone's hw on github  as a reference because I couldn't understand some things, so this hw is not my own
# for 100% :(
class Fish:
    '''This class contains defferent kinds of fish their attributes and methods'''
    weight: 10

class CatFish(Fish):
    lengthOfWhiskers = 52

    def __repr__(self):
        return CatFish.__name__

class Carp(Fish):
    color = 'blue'

    def __repr__(self):
        return Carp.__name__

class UserFish(Fish):
    def __init__(self, name, size, weight):
        self.name = name
        self.size = size
        self.weight = weight

def __repr__(self):
    return self.name
