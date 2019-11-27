class Animal:
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def details(self):
        print(self.name)


c = Cat("Mycat")
c.details()


class Vehicle:
    def __init__(self):
        pass

    def Driving(self):
        print("Driving the Car")

    def __PrintDetails(self):  # privat method not accessible
        print("Print Details")


v = Vehicle()
v.Driving()


class Car:
    def __init__(self):
        self.__price = 3000

    def PrintDetails(self):
        print(self.__price)

    def setPrice(self, newprice):
        self.__price = newprice


c = Car()
c.PrintDetails()

c.setPrice(5000)
c.PrintDetails()
