#try:
#except:
#else:
#finally:
while True:
    try: # try runs to see if there is a problem or not  ** commonly use
        num = int(input("please enter a number: "))
    except ValueError:# if theres a problem, except will run  ** commonly use
        #specify the error!!!!
        print("That's not a number!")
    else: #if theres no problem, else will run
        print ("Good job you entered a number!")
        break
    finally: # will runs no matter what # not commonly used
        print ("RUNS NO MATTER WHAT!")
print ("rest of game logic!")
###########
######################## Example

def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
    #can also combine both error
    #except (ZerdivisionError, Type Error) as err:
        #print "something went wrong"
        #print (err) print out which error
        print ("Dont divide a 0 please")
    except TypeError as err:
        print ("a and b must be int or float")
        print (err) #print out the type error from that raise 
    else:
        print (f"{a} divided by {b} is {result}")
    
print (divide(1,2))
print (divide(1,0))
print (divide(1,'ab'))