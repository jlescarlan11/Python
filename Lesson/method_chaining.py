"""
method chaining =   calling multiple methods sequentially
                    each call performs an action on the same object and return self
"""

class Car:

    def turn_on(self):
        print("You start the engine")
        return self
    
    def drive(self):
        print("You drive the car")
        return self
    
    def brake(self):
        print("You step on the brakes")
        return self
    
    def turn_off(self):
        print("You turn off the engine")
        return self
    
car = Car()


#   You can cut this by using \
car.turn_on().drive().brake().turn_off()

#   Like this
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
