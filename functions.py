def print_hello():
    print("Hello world")


print_hello()


def print_hello_name(name="Default"):
    print("Hello " + name)


print_hello_name("Sebastian")
print_hello_name()


def number_multiply(x):
    return 7 * x


print(number_multiply(2))
print(number_multiply(10))
