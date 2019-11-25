class A:
    def move(self):
        print("Moving...")


class B(A):
    def eat(self):
        print("Eating...")


class C(B):
    def walk(self):
        print("Wakling")


b = B()
b.move()
b.eat()

c = C()
c.eat()
c.move()
c.walk()


class D(C):
    def jumping(self):
        print("Jumping")


d = D()
d.jumping()
