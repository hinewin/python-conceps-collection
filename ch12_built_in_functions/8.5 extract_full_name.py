# extract_full_game - accepts a list of dict
# return a new list of strings with 
# first & last name keys in each dict concatenated

names= [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

# def extract_full_game(dic):
#     return [f"{char['first']} {char['last']}" for char in dic]
#extract_full_name(names) # ['Elie Schoppik', 'Colt Steele'


def extract_full_name(dict):
    return list(map(lambda char : "{} {}".format(char ['first'],char['last']), dict))
# map (to iterate) for each char in dict,
# {}{}/ 1st{}= first name, 2nd {} = last for each item in DICT
print (extract_full_name(names))