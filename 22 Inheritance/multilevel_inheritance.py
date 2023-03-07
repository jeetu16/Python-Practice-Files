# multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating")
class Dog(Animal):
    def __init__(self, clr):
        self.color = clr
    def bark(self):
        print("This dog is barking")


dog = Dog('red')
print(dog.alive)    # accessing super parent(grand parent) property
dog.eat()           # accessing parent class method

