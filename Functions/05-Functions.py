def add(x,y):
    z = x + y
    print("Sum is",z)
    return z

def sub(x,y):
    z = x - y
    print("Sub is",z)

def calc():
    x = 5
    y = 8
    z = add(x,y)
    sub(z,y)

calc()