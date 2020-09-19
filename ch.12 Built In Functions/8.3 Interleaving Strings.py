#function interleave accepts two strings
#return new string contatining the 2 strings interwoven/zipped
#ex interleave('hi','ha') # hhia

def interleave(str1,str2):
    return list(
        map(lambda char:(f"{char}{str2}")(zip(str1,str2)))
        )











print (interleave('hi','ha'))