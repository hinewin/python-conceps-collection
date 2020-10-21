#Keep track of how many eggs each chicken lays
# Track total number of eggs all hens have laid
# Chicken class, each Chicken has a species and name
# has an integer attribute Eggs (starts out at 0)
#Each chicken has an instance called lay_egg()
#Increment & return Chicken's eggs attribute
#lay_egg() increment class variable called total_eggs


class Chicken:
    total_eggs = 0 # class variable, increments each time egg is laid
    def __init__(self,species,name):#class attributes
        self.species = species
        self.name = name
        self.eggs = 0 #integer attribute egg should always start a 0
    def lay_egg(self):
        self.eggs += 1 # each time lay_egg is called, add 1 in attribute eggs
        Chicken.total_eggs += 1 #total will be added up 
        return self.eggs