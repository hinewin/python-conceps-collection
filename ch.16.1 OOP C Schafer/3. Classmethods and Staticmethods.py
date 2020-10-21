class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +"."+ last + "@company.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'
    def apply_raise(self):
        self.pay = int(self.pay *self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

emp_1 = Employee('Corey','Schafer','5000')
emp_2 = Employee ('Test','User',6000)

#to take an instance as the first argument use Self
# So how could we take CLASS as the first argument?
# to turn regular method to class method use decorator @classmethod

#if we set set_raise_amt to 1.05, instances will be changed
Employee.set_raise_amt(1.05) #Now we will change the class variable using cls method
print (Employee.raise_amt) # 1.04 >> 1.05
print (emp_1.raise_amt) # 1.04 >> 1.05
print (emp_2.raise_amt) #1.04 >> 1.05