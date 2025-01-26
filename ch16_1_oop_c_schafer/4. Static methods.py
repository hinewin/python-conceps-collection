class Employee:
    num_of_emps = 0
    raise_amt = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +"."+ last + "@company.com"

    def fullname(self):
        return f'{self.first} {self.last}'
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)
    
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str_1.split('-')
        return cls(first,last,pay)


    @staticmethod #if were not referring a class or instance, use static method
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False 
        return True

emp_1 = Employee('Corey','Schafer','5000')
emp_2 = Employee ('Test','User',6000)

#### 
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

#static method dont pass using first argument like class or instance
#test out static method
import datetime
my_date = datetime.date(2016,7,10)

print (Employee.is_workday(my_date)) #not in the weekday