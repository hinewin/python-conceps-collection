class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +"."+ last + "@company.com"

        Employee.num_of_emps += 1 # each time init is ran we add 1 more user


    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self): # this requires a manual update
        self.pay = int(self.pay * self.raise_amount) 
    # we want to apply it to a class variable instead of instance
    #to use a class variable, use the class name.variable or self/instance


print (Employee.num_of_emps) #output is 0 because we didnt create any

emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee ('Test','User',60000)

print (Employee.raise_amount)
print (emp_1.raise_amount)
#when were accessing it from the instance, we are accessing
#the classes attributes
print (emp_2.raise_amount)
#The instances are not accessing it themselves 
# this is the CLASS variable which is 1.04

print (emp_1.__dict__)
1.04
#output of this instance in dict form: 
# {'first': 'Corey', 'last': 'Schafer', 'pay': 50000,
#  'email': 'Corey.Schafer@company.com'} 
# no raise amount because its in the CLASS 

#Employee.raise_amount = 1.05
print (emp_1.raise_amount) #output changes as we changed the value

# No what will happen if we change raise amount for the instance?
emp_1.raise_amount = 1.05
print (emp_1.raise_amount) #will change to 1.05
print (emp_2.raise_amount) # will stay as 1.04

#now check emp_1 dict
print (emp_1.__dict__) #now raise amount will be part of the instance 

print (Employee.num_of_emps) # should be 2 users since its after