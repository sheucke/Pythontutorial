# objects
x = 5
y = 'string'
y.strip()  # method strip on the instance of class str

print(type(x))
print(type(y))

print(help(int))


# create a new class

class Dog(object):
    # constructor , always happens when creating a class
    def __init__(self, name, age):  # takes parameters
        self.name = name
        self.age = age
        print("Nice you made a dog object!")

    def speak(self):
        print('Hi I am', self.name, 'and I am', self.age, 'years old.')

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight


tim = Dog('Tim', 56)
tim.speak()
fred = Dog('Fred', 3)
tim.change_age(5)
tim.add_weight(70)
tim.speak()
fred.speak()

print(tim.age)
print(tim.name)
print(tim.weight)
