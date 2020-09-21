# Create your own exception / error messages using "raise"
#** raise ValueError ('invalid value')

def colorize (text,color):
    colors = ("cyan","yellow","blue","green","mageneta")
    if type(text) is not str:
        raise TypeError("text must be a str")
    #specify each error to be clear which parameter
    if type(color) is not str:
        # if parameter txt is not a str raise this error
        raise  TypeError("color must be instance of str")
    if color not in colors:
        raise ValueError ("Color is invalid color")
    print (f"Printed {text} in {color}")

colorize ("Hello","red")
