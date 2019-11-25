class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def PrintDetails(self):
        print("My Name is: " + self.name, "My Age is: " + str(self.age))


class Student(Person):
    pass


st1 = Student("Parwitz", 24)
st1.PrintDetails()

st2 = Student("Hohn", 30)
st2.PrintDetails()
