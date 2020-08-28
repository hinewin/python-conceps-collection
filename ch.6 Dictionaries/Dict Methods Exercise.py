# With provided inventory variable
# Copy inventory to variable stock_list
# Add value 18 to stock list under cookie
#Remove "cake" from stock_list


inventory ={'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}
stock_list=inventory.copy()
print(stock_list)
stock_list["cookie"]=18
stock_list.pop("cake")
print(stock_list)