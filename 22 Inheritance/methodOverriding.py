class Animal:
    def eat(self,name):
        print("This animal is eating")


class Rabbit(Animal):
    # here child class method eat() overrides parent class method eat()
    def eat(self):      
        print("This aniamal is eating a carrot")
    pass


rabbit = Rabbit()

# error becuase of child class doesn't have method eat() which takes an argument
# rabbit.eat('jd')

# here child class object rabbit calls eat() method which is present in child class. if eat() method doesn't find in child class then it goes to their parent class and finds eat() method.
rabbit.eat()        