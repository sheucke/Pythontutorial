class Dog(object):
    # constructor , always happens when creating a class
    def __init__(self, name, age):  # takes parameters
        self.name = name
        self.age = age
        print("Nice you made a dog object!")

    def speak(self):
        print('Hi I am', self.name, 'and I am', self.age, 'years old.')


class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color


tim = Cat('tim', 5, 'black')
tim.speak()
