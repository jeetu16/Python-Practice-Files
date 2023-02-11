class Animal:
    alive = True
    def __init__(self,nm):
        self.name = nm
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Rabbit(Animal):
    def run(self):
        print(f"{self.name} is running")
class Fish(Animal):
    def swim(self):
        print(f"{self.name} is swimming")
class Hawk(Animal):
    def fly(self):
        print(f"{self.name} is flying")

rabbit = Rabbit('Harry the rabbit')
fish = Fish('David the fish')
hawk = Hawk('John the hawk')

print("Name :",rabbit.name) # acessing parent class instance varialbe
print(f"Is {rabbit.name} alive ? {rabbit.alive}")
rabbit.eat()                # accessing parent class method
rabbit.run()                # accessing own class method