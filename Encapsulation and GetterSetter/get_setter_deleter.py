class Fruit:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, other_age):
        if other_age <= 0:
            raise ValueError('omg, age must be more than zero!')
        else:
            self._age = other_age
            
    @age.deleter
    def age(self):
        print("deleting the age!")
        del self._age


watermelon = Fruit('watermelon', 45)

    
watermelon.age = 34
print(watermelon.age)

del watermelon.age

try:
    print(watermelon.age)
except AttributeError:
    print("You deleted the age above! huhh")









