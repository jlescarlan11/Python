"""
duck typing =   concept where the class of an object is less important than the methods/attributes
                class type is  not checked if minimum methods/attributes are present
                "If it walks like a duck, and it quacks like a duck, then it mest be a duck"
"""

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuaking")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():

    def catch(self,duck):
        # Using duck typing: We don't care about the specific class/type of the object,
        # as long as it has the 'walk' and 'talk' methods.
        duck.walk()
        duck.talk()
        print("You caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)