class Animal:

    def eat(self):
        print("The animal is eating")

class Rabbit(Animal):

    def eat(self):
        print('This animal is eating a carrot')

rabbit = Rabbit()

rabbit.eat()
animal = Animal()
animal.eat()