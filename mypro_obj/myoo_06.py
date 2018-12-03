class Employee:

    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        if 1000<salary<500000:
            self.__salary = salary
        else:
            print("录入错误！薪水在1000——500000这个范围")

emp1 = Employee("NCT",30000)
print(emp1.get_salary())
emp1.set_salary(100000)
print(emp1.get_salary())
