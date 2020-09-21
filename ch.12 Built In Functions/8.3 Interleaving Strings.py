#function interleave accepts two strings
#return new string contatining the 2 strings interwoven/zipped
#ex interleave('hi','ha') # hhia

def interleave(str1,str2):
    return "".join(("".join(char) for char in (zip(str1,str2))))

#Breakdown 

#first zip the two lists first two get the two tuples (h,h), (i,a)
print(list(zip("hi",'ha'))) ## (h,h), (i,a)
#now convert the tuple into strings
print (list("".join(char) for char in zip("hi","ha")))
#["hh","ia"]
#last step would to convert those strings together
print ("".join("".join(char) for char in zip("hi","ha")))
##hhia


print (interleave('hi','ha'))