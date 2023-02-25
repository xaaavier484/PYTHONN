
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print(f"Hello, my name is {self.name} and my age is {self.age}")
#Creating my object
person1=Person("Xavier",16)
person1.say_hello()
person2=Person("Adam",18)
person2.say_hello()
person3=Person("Zara",17)
person3.say_hello()
   #Create a class called cars with the following attributes/properties
   #make.model.year then create a function that prints make,mode and year
   #then create three obhtexts
class car:
    def __init__(self, modelname, year):
        self.modelname = modelname
        self.year = year

    def display(self):
        print(self.modelname, self.year)


c1 = car("Rolls Royce", 2022)
c1.display()
c1 = car("Hyundai", 2011)
c1.display()
c1 = car("Mitsubishi", 2019)
c1.display()
c1 = car("Mercedes", 2021)
c1.display()
c1 = car("Tesla", 2023)
c1.display


