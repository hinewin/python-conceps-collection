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
    #new codes:
    @classmethod
    def from_string(cls,emp_str):#alternative constructor starts with from
        first,last,pay = emp_str_1.split('-') #store the value from the string
        return cls(first,last,pay) #generate a new user instead of using the CLASS
        #we can use cls since we are inside a class method
    

emp_1 = Employee('Corey','Schafer','5000')
emp_2 = Employee ('Test','User',6000)


#If each entry is a string seperated by '-'
# we could create an account using this info

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'
# we could split the string first,last,pay = emp_str_1.split('-')
#then make new_emp_1 = Employee (first,last,pay)
#However we can make can make a class for this

#now instead of parsing the string, we can run the new string method
new_emp_1 = Employee.from_string(emp_str_1)
print (new_emp_1.email) #John Doe 