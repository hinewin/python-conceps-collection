class Employee:
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +"."+ last + "@company.com"

    def fullname(self):
        return f'{self.first} {self.last}'
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):# New codes: Initiate more instances
    raise_amt = 1.10 
    def __init__(self,first,last,pay, prog_lang): #add new argument (prog_lang)
        #Take first/last/email/pay from Employee, but well make prog_lang
        super().__init__(first,last,pay) #Employee will handle these arguments
        #Employee.__Init__(self,first,last,pay) # works as well
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay, employees=None): #dont set mutable data type (list/dict)
        super().__init__(first,last,pay)                            #as default argument.
        if employees is None:
            self.employees = [] #if none, set to empty list
        else:
            self.employees = employees #set them to employee lists if its not none

    def add_emp(self,emp):
        if emp not in self.employees: #if emp not in the emp list already
            self.employees.append(emp) #add emp in the list
    def remove_emp(self,emp):
        if emp in self.employees: #if emp in the emp list already
            self.employees.remove(emp) #remove the emp
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer ('Corey','Schafer',5000,'Python')
dev_2 = Developer ('Test','Employee',6000,'Java')

mgr_1 = Manager ('Sue','Smith','90000',[dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2) #adding dev_2 into mgr emp[list]
mgr_1.remove_emp(dev_1)

mgr_1.print_emps() #printing out the employees list from mgr_1

#######################################
#isinstance = tell us if an object is an instance of a class
print (isinstance(mgr_1, Manager)) #checking if mgr_1 is an instance of class Manager #True
print (isinstance(mgr_1, Employee)) #mgr_1 is an instance of Employee #True
print (isinstance(mgr_1,Developer )) #is mgr_1 an instance of Developer? #False
#Nope, they both inher from EMPLOYEE but not each other inheritance 

#issubclass- Tell if a CLASS is a subclass of another
print(issubclass(Developer,Employee)) #Is developer a subclass of an employee # True
print(issubclass(Manager,Developer)) #Is manager a subclass of an developer? # False

