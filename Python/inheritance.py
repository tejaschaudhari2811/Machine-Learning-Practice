# base class
class Animal:

    def eat(self):
        print("I can eat")
    
    def sleep(self):
        print("I go to sleep now.")

# Derived class or Child class
class Dog(Animal):

    def bark(self):
        print("I can bark. WOOF!")

# Create an object of dog class
dog = Dog()

# Call methods of base class
dog.eat()
dog.sleep()
dog.bark()