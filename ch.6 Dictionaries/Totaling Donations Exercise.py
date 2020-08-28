#Given dictionary, use to calculate total value of the donatio ns
donations = dict(sam=25.0, lena=88.99,chuck=13.0,linus=99.5,stan=150.0,lisa=50.25,harrison=10.0)
total_donation = 0
for num in donations.values():
    total_donation += num
    print (total_donation)