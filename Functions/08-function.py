def calc(x,y):
    z1 = x + y
    z2 = x - y
    z3 = x / y
    z4 = x * y
    return z1, z2, z3, z4

# a = calc(4,5)
# print(a)
# packing and unpacking
a,b,c,d = calc(4,5)
print("Sum is",a)
print("Sub is",b)
print("Div is",c)
print("Mul is",d)