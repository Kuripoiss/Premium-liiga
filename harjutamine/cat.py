class Car:

    wheels = 4



    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This "+self.make+" is driving")

    def stop(self):
        print("This "+self.make+" has stopped")