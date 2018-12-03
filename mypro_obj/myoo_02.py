class Student:

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def say_score(self):
        print("{0}的分数是：{1}".format(self.name,self.score))

stu2 = Student
s1 = Student("jaemin",100)
s2 = stu2("mark",100)

s1.say_score()
s2.say_score()