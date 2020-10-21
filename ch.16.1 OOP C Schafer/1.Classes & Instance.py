class Employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first +''+'@company.com'
#what is self?
#Each method in a class take the instance (emp_#)
# as the 1st argument (self)
#
    def fullname(self): # the function will be applied to the 
        #argument self (aka the instance)
        return f"{self.first} {self.last}"

emp_1 = Employee('Corey','Schafer',5000) # these are instances of the EMPLOYEE class
emp_2 = Employee('Test','User',6000) # these are instances of the EMPLOYEE class

print (emp_1)
print (emp_2)

# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'Corey.Schafer@company.com'
# emp_1.pay = 50000
#       # No need to manually add each user info since we have a class
# emp_2.first = 'Corey'
# emp_2.last = 'Schafer'
# emp_2.email = 'Corey.Schafer@company.com'
# emp_2.pay = 60000

print (f'{emp_1.first} {emp_1.last}') # that's too long to print first & last
# we will create the method fullname
print (emp_1.fullname()) #print instance emp1 with function fullname

#similarly, you can run using class
#if we want to run as a class, you must pass in which instance
print (Employee.fullname(emp_1)) #class.function(instance)