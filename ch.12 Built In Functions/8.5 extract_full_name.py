# extract_full_game - accepts a list of dict
# return a new list of strings with 
# first & last name keys in each dict concatenated

names= [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

def extract_full_game(dic):
    return list (map(lambda c: "{c['first']} {c['last']}", dic))
#extract_full_name(names) # ['Elie Schoppik', 'Colt Steele'

print (extract_full_game(names))