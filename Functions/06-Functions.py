# Packing and Unpacking

def calc(x,y):
    z1 = x + y
    z2 = x - y
    z3 = x / y
    z4 = x * y
    return z1, z2, z3, z4

# add = calc(5,6)
# print(add)

# print(calc(4,5))
# a,b,c,d = calc(4,5)
# print("Add is",a)
# print("Sub is",b)
# print("Div is",c)
# print("Mul is",d)

a,b,*c = calc(4,5)
print("Add is",a)
print("Sub is",b)
print("Div and Mul is",c)
