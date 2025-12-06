# Python Class and Object
class Parrot:
    # class attribute
    name = ""
    age = 0
# Create parrot1 object
parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10
# Create another object parrot2
parrot2 = Parrot()
parrot2.name = "Woo"
parrot2.age = 15
# Access Attributes
print(f"{parrot1.name} is {parrot1.age} years old.")
print(f"{parrot2.name} is {parrot2.age} years old.")
# Base Class
class Aninmal:
    def eat(self):
        print("Eating")
    def sleep(self):
        print("Sleeping")
# Derived Class
class Dog(Aninmal):
    def bark(self):
        print("Barking")
# Create Dog object
dog1 = Dog()
dog1.bark()
dog1.eat()
dog1.sleep()
class computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print(f"selling Price: {self.__maxprice}")
    def setMaxPrice(self, price):
        self.__maxprice = price
c = computer()
c.sell()
# change the price
c.setMaxPrice(1000)
c.sell()
# Using setter function
c.setMaxPrice(1000)
c.sell()