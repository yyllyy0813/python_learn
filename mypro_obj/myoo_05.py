class Employee:

    @property
    def salary(self):
        print("salary running")
        return 10000

emp1 = Employee()
#emp1.salary()
print(emp1.salary)