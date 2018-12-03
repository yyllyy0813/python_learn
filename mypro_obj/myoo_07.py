class Person:

    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def say_age(self):
        print("NCT")

class Student(Person):

    def __init__(self,name,age,score):
        Person.__init__(self,name,age)   #必须显示调用
        self.score = score

print(Student.mro())  #可打印类的层次

s = Student("jaemin",18,100)
s.say_age()
print(s.name)
#print(s.age)
print(s._Person__age)

print(dir(s))