midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']
# Say the first number in each list is the score of each person
# We want to show the highest grade for each person

# get a pair of tuple per person name
print ([pair for pair in zip(midterms,finals)])
#Now you want the max per pair
# print (max([pair for pair in zip(midterms,finals)]))
#*** (91,89)
## this would print the MAX PAIR in all pairs instead of EACH

#to print the max value in EACH pair
print ([max(pair) for pair in zip(midterms,finals)])
#98,91,78

# Now we want a dictionary, name of student and their score
print ({pair[0]: max(pair[1],pair[2])for pair in zip(students,midterms,finals)})
#dan:98, ang:91, kate:78

#since we cannot get the max of students ([0])
#get max of midterms & finals [1] & [2] in a dict called pair
#dict pair contains students[0],midterm[1],finals[2]
# using student name as the key and highest scores as values
#{pair[0]:highest score from midterm and finals



### USING LAMBDA
scores = map(
lambda pair: max(pair),
zip(midterms,finals)
)
#use map to iterate 
#for each pair, find the max of the pair, in list (zip(midterms,finals))
print(list(scores))

#Now we want to add the student names
grades = zip( # a clever way to do this is to do a zip of students & score
    students, # using zip will match the first value (name)
    #with the other first value(score)
    map(lambda pair: max(pair),zip(midterms,finals))

)

print (dict(grades))

########## To find the AVERAGE of the pair 
avg_grade = dict( #make it clean print dict
zip(students, # zip both students, score
map(lambda pair:((pair[0]+pair[1])/2),zip(midterms,finals))))
# for each pair in zip(score), add them and /2
print (avg_grade)