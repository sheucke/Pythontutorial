class A:
    def move(self):
        print("Moving....")


class B:
    def eat(self):
        print("Eating...")


class C(A, B):
    pass


c = C()
c.move()
c.eat()


class Person:
    def __init__(self):
        print("Please Enter Your Details")
        self.name = input("Enter Name: ")
        self.lname = input("Enter Lastname: ")
        self.phone = input("Enter Phone: ")
        self.age = input("Enter Age: ")

    def PrintDetails(self):
        print("\n\nName: ", self.name)
        print("Lastname: ", self.lname)
        print("Phone Number: ", self.phone)
        print("Age:", self.age)


class StudentMarks:
    def __init__(self):
        print("Please enter your marks")
        self.math = int(input("Math Mark :"))
        self.history = int(input("History Mark: "))
        self.programming = int(input("Programming Mark: "))

    def PrintDetails(self):
        totalExamMarks = self.math + self.history + self.programming

        if totalExamMarks < 80:
            print("Total Exam Marks: " + str(totalExamMarks))
            print(" you failed")

        else:
            print("Total Exam Marks: " + str(totalExamMarks))
            print("You are succesfull")


class Student(Person, StudentMarks):
    def __init__(self):
        Person.__init__(self)
        StudentMarks.__init__(self)

    def PrintDetails(self):
        Person.PrintDetails(self)
        StudentMarks.PrintDetails(self)


student1 = Student()
student1.PrintDetails()
