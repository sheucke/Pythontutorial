# lambda arguments: expression


def x(a): return a+5


print(x(5))


def x(a, b): return a * b


print(x(5, 4))


def my_function(n):
    return lambda a: a * n


myFunc = my_function(3)

print(myFunc(11))
