# multiple inheritance = when a child class is derived from more than one parent class

class Prey:
    def flee(self):
        print("This animal flees")

class Prediator:
    def hunt(self):
        print("This animals is hunting")

class Rabbit(Prey):
    pass

class Hawk(Prediator):
    pass

class Fish(Prey,Prediator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

# rabbit.flee()
# hawk.hunt()

fish.hunt()
fish.flee()