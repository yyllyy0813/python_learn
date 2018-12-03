class Student:

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def say_score(self):
        print("{0}的分数是：{1}".format(self.name,self.score))

s1 = Student('jaemin',100)
s1.say_score()

s1.age = 18
s1.salary = 30000
#del s1

print("salary is",s1.salary)

s2 = Student("mark",100)
s2.say_score()

print(dir(s2))
print(s2.__dict__)
print(isinstance(s2,Student))

class Man:
    pass
print(isinstance(s2,Man))