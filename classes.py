class My_class:
    pass


class1 = My_class()
class2 = My_class()

print(class1)
print(class2)


class Employee:
    pass


emp1 = Employee()
emp2 = Employee()

emp1.firstName = "Parwiz"
emp1.email = "sebastian@email.de"
emp1.salary = 3000

emp2.firstName = "John"
emp2.email = "john@email.de"
emp2.salary = 4000

print("First Name: " + emp1.firstName)
print("Salary: " + str(emp2.salary))


class Employee1:
    def fullName(self):
        self.firstname = "Sebastian"
        self.lastname = "Heucke"


emp1 = Employee1()
emp1.fullName()
print(emp1.firstname, emp1.lastname)


class Employee2:
    def fullName1(self, firstName, lastname):
        self.firstName = firstName
        self.lastname = lastname

        print(firstName + lastname)


emp1 = Employee2()
emp1.fullName1("Sebastian ", "Heucke")
