class Person:

    def __del__(self):
        print("销毁对象{0}".format(self))

p1 = Person()
p2 = Person()
print(id(p1))
print(id(p2))
del p2
print("程序结束标记")