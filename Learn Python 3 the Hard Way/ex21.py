def var_info(a):
    b = type(a)

    print(f"value : {a}\ntype : {b}")


def add(a, b):
    print(f"ADDING {a} + {b}")
    return a+b


def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a-b


def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a*b


def divide(a, b):
    print(f"DEVIDING {a} / {b}")
    return a/b


a = add(1223, 2233)
print(a)
b = subtract(3434, 1123)
print(b)
c = multiply(a, b)
print(c)
d = divide(c, a)
print(d)
var_info(d)