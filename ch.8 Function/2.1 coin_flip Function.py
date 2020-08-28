from random import random

def flip_coin():
    # generate random num (0-1)
    r = random()
    if r >= 0.5:
        return "Heads"
    else:
        return "Tails"

print (flip_coin())

### better function

def bflip_coin():
    if random()>= 0.5:
        return "Heads"
    else:
        return ("Tails")
print(bflip_coin())