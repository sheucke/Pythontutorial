class A:
    def __init__(self, name, lastname):

        self.name = name
        self.lastname = lastname

    def PrintDetails(self):
        print("My name is " + self.name + self.lastname)


class B(A):
    def __init__(self, name, lastname, email):
        super().__init__(name, lastname)
        self.email = email


a = A("John ", "Doe")
a.PrintDetails()

b = B("Sebastian ", "Heucke")
b.PrintDetails()
