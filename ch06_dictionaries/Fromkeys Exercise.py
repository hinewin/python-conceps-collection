# use dict.fromkeys to generate new dict from provided
## game_properties list. Initialize all values to 0
# Save result in initial_game_state
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 
initial_game = dict.fromkeys(game_properties,[0])
# variable = for each key in game properties, set value to 0
#Fromkeys (key,value**for each key**) 
print (initial_game)
