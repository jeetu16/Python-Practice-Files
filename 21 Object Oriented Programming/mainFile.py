from Car import Car


car1 = Car("Audi",'Gray',2022)
car2 = Car("BMW",'Black',2020)

Car.wheels = 2      # we can change class variable value
car1.wheels = 4     # as well copy of class variable for instance of object


print("This " + car1.color + " color " + car1.name +
      " is luanched in", car1.year,". And it has",car1.wheels,"Wheels")      # accessing class property

car2.drive()    # accessing class method
car2.stop()