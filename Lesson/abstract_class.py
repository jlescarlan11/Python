"""
Prevents a user from creating an object of that class
+ compels a user to override abstract methods in a child class

abstract class = a class which contains one or more abstract methods.
abstract method = a method that has a declaration but does not have an implementation.
"""

from abc import ABC, abstractmethod

# Define an abstract class 'Vehicle' using ABC (Abstract Base Class)
class Vehicle(ABC):

    # Declare abstract method 'go' without providing implementation
    @abstractmethod
    def go(self):
        pass

    # Declare another abstract method 'stop' without providing implementation
    @abstractmethod
    def stop(self):
        pass

# Concrete subclass 'Car' inheriting from the abstract class 'Vehicle'
class Car(Vehicle):
    
    # Provide implementation for the abstract method 'go'
    def go(self):
        print("You drive the car")

    # Provide implementation for the abstract method 'stop'
    def stop(self):
        print('This car has stopped')

# Concrete subclass 'Motorcycle' inheriting from the abstract class 'Vehicle'
class Motorcycle(Vehicle):

    # Provide implementation for the abstract method 'go'
    def go(self):
        print("You ride the motorcycle")

    # Provide implementation for the abstract method 'stop'
    def stop(self):
        print("This motorcycle has stopped")

# Attempt to instantiate the abstract class 'Vehicle' directly would raise an error
# vehicle = Vehicle()

# Instantiate the concrete subclass 'Car'
car = Car()

# Instantiate the concrete subclass 'Motorcycle'
motorcycle = Motorcycle()

# Attempting to call abstract methods on an instance of an abstract class would raise an error
# vehicle.go()

# Call methods on instances of concrete subclasses
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()
