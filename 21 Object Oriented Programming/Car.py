class Car:

    wheels = 4                  # class variable (outside of __init__())

    def __init__(self,nm,clr,yr):
        self.name = nm          # instance variable
        self.color = clr        # instance variable
        self.year = yr          # instance variable
    
    def drive(self):
        print("This " + self.name +" is driving")
    def stop(self):
        print("This " + self.name + " is stopped!")