# write a function called **return_day**
# Takes in one paramter (number between 1-7)
# Returns the day of the week (1=sunday, 2=Monday,etc)
# If number <1 or >7 return none
# hint store days of the week in a dict

days = {1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",7:"Saturday"}
def return_day(day):
    if day in days:
        return days[day]
    return None

print(return_day(4))
 
 ########
#           ALTERNATIVE SOLUTION
 ####

def return_day2(num):
    days = {1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",7:"Saturday"}
    if num > 0 and num <= len(days):
        return days[num-1]
    return None
print (return_day2(4))