a = 20
b = 30
c = a+b
d = a.__add__(b)
print("c=",c)
print("d=",d)
print(id(c))
print(id(d))