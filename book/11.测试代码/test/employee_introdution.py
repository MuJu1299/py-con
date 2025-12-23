class Employee:
    '''储存元购的姓名和工资'''
    def __init__(self,first,last,salary):
        self.first=first
        self.last=last
        self.salary=salary

    def give_raise(self,increase_salary=5000):
        self.salary+=increase_salary
        