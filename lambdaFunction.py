# Lambda Tutorial


def func(x):
    def func3(x): return x+10
    return func3(x) + 85


print(func(2))


def func2(x): return x+5


print(func2(9))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newList = list(map(lambda x: x+5, a))
newList1 = list(filter(lambda x: x % 2 == 0, a))
print(newList)
print(newList1)
