# Parameter Ordering
# 1) Parameters
# 2) #args
# 3) default parameters
# 4) **kwargs

def display_info (a,b, *args,instructor ="Colt", **kwargs):
    return [a,b,args,instructor,kwargs]
print (display_info(1,2,3, last_name ="Steele", job ="Instructor"))
#output:
#a - 1
#b - 2
# args - (3)
# instructor = none (Colt)
# **kwargs= {"lastname": "Steele", "job": "instructor"}