from abc import ABC, abstractmethod

class Fruit(ABC):
    @abstractmethod
    def taste(self):
        pass
    
"""taste method must be used below by every child class of Fruit"""
class Mango(Fruit):
    def taste(self):
        return ('Mango is delicious.')
        
class Watermelon(Fruit):
    def taste(self):
        return('Watermelon is sweet.')
class Kiwi(Fruit):
    def taste(self):
        return('Kiwi is salty')
        
m = Mango()
print(type(m) is Fruit)
print(m.taste())

k = Kiwi()
print(k.taste())


#output
"""False
Mango is delicious.
Kiwi is salty"""
