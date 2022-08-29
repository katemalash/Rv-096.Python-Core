class Pond:
    '''It is a class which tells us about attributes and methods of the pond'''

    capacity = list()

    def state(self):
        if len(self.capacity) < 5:
            return 'poor'
        elif len(self.capacity) <= 10:
            return 'normal'
        else:
            return 'rich'

    def obtainFish(self, Fish):
        return self.capacity.append(Fish)

    def lostFish(self, Fish):
        return self.capacity.pop(Fish)

    def showCapacity(self):
        return print(self.capacity)

    def showState(self):
        return print(self.state())
