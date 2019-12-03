class Dog:
    dogs = []  # specific to entire dog class

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod  # decorator specify a class method
    def num_dogs(cls):  # cls means name of the class
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        """barks n time"""
        for n in range(n):
            print("Bark!")


tim = Dog("Tim")
jim = Dog("Jim")
print(Dog.num_dogs())  # calling a class method
