#   Animal is the parent class
class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

"""
The benefit of inheritance is that you dont need to add the attributes to the child class
"""

"""
Do note that each classes can have their own attribute
"""
#   Rabbit class is the child class
class Rabbit(Animal):
    pass

class Fish(Animal):
    pass

class Hawk(Animal):
    pass

#   this is called object
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)

fish.eat()
hawk.sleep()