class Car:
    
    wheels = 4  #   This is an example of class variable
    def __init__(self, make, model, year, color):   #   init method is class constructor
        #   Attributes describes the car
        self.make = make    #   This is known as instance variable
        self.model = model
        self.year = year
        self.color = color

    #   What method can Attributes perform
    def drive(self):
        print(f"This {self.model} os driving")

    def stop(self):
        print(f"This {self.model} stopped")