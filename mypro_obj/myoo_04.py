class SalaryAccount:

    def __call__(self, salary):
        yearSalary = salary*12
        daySalary = salary//30
        hourSalary = daySalary//8
        return dict(monthSalary = salary,yearSalary=yearSalary,daySalary=daySalary,hourSalary=hourSalary)

s = SalaryAccount()        #先创建一个对象再使用
print(s(5000))             #可以像调用函数一样调用对象的__call__方法