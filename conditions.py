a = 20
b = 30

if a < b:
    print("a is smaller than b")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


a = 40
b = 20

if a > b:
    print("a is greater than b")

print("a is greater than b") if a > b else print("b is greater than a")
