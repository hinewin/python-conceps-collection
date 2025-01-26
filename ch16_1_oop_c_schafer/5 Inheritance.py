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

class Developer(Employee): #We are inherenting from Employee class
    #We will be able to use attributes/methods from employee class
    raise_amt = 1.10 #changing the attribute in our sub-class will make changes
    #only in the sub-class and not MAIN class

dev_1 = Developer ('Corey','Schafer',5000)
dev_2 = Developer ('Test','User',6000)

# print(dev_1.email)
# print(dev_2.email)

print (dev_1.pay)
dev_1.apply_raise()#using the Employee raise method but if we add our own
#raise_amt under Developer, the output willl be different
print(dev_1.pay)