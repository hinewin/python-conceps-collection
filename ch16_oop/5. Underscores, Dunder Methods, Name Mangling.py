#_name ## single underscore is private attribute/method
#__name 2 Underscore - Name mangle, change the name of that attribute
#__name__ #dunder methods( 1 single then 2 underscore)


class Person:
    def __init__(self): #"magic methods within Python"
        self.name = "Tony"
        self._seret = "hi!" #private method
        self.__msg = "I like turtles!" #name mangle
        self.__lol = "hahaha"
#single is NOT intended to use the attribute outside of the class
# single underscore = private variable

p = Person()
print (p.name)
print (p._seret)
#print (dir(p)) 
#2 underscores before name/attribute is name mangling
#to access the name mangling use single doublescore and double
print (p._Person__msg)
print (p._Person__lol)

