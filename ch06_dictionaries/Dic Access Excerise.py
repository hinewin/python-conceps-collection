#module generate a random food item in list
# Print out a string from bakery stock depending on food

from random import choice
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])

bakery_stock={
 "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25

}
## ex if food = tea cake, print "25 left" else "We Dont make that"

if food in bakery_stock: ## if food items are in the bakery list
    print (f"{bakery_stock[food]} left") # print [food] which is the value
    # print the value of food in bakery stock if food exists
    print (food)
else:
    print ("We don't make that")