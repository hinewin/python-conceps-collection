playlist = { ### Playlist variable contains a dictionary
    "title": "Simp",# Within the dict, each keys have dif values
    "author": "Hai",
    "songs": [ # Song key is a list (so can itterate within songs)
    {"title": "Thinking about you", "artist": ["Frank Ocean"],"duration": 2.5},
    {"title": "Blessed", "artist": ["Daniel Caesar"], "duration": 3.20},
    {"title": "Japanese Denim", "artist":["Daniel Caesar"], "duration": 4.20}
 #title is key, artist is key, but artist key contains a list
 #duration is key value
 ]
}
#Ex: Get the total duration length
total_length = 0 #First set the variable to empty (0)
for song in playlist ["songs"]: #You want the list in songs
    #Get value "song" in key"songs" in variable playlists,
    total_length += song["duration"]
    #Add the length of each duration up
    print (total_length)
