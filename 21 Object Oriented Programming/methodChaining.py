# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self


class Car:

    def turnOn(self):
        print("You start the engine!")
        return self

    def drive(self):
        print("You drive the car!")
        return self
    
    def brake(self):
        print("You step on the brake!")
        return self

    def turnOff(self):
        print("You turn off the engine!")
        return self


car = Car()

# method chaining
car.turnOn().drive().brake().turnOff()

# here \ is used for continue of line
car.turnOn()\
   .drive()\
   .brake()\
   .turnOff() 
