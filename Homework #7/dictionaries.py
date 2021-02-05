'''
This file gives as many details about my favourite song in the form of
key : value pairs in a dictionary.
The function guess() returns true if the key is present in the dictionary
and the value of the key is equal to the argument Value of the function.
'''


dictionary = {
    "SongTitle":"Enjoy the silence",
    "Artist":"Depeche Mode",
    "Genre":"Synth-pop",
    "AlbumTitle":"Violator",
    "YearRecorded":1989,
    "YearReleased":1990,
    "Length":372,                        # duration of song in seconds
    "Studio":"Puk (Gjerlev, Denmark)",   # the name of the studio
    "Songwriter":"Martin Gore",
    "LabelName":"Mute Records Ltd.",
    "VinylSize":7.0                      # the size in inches of the vinyl disk
    }                  

for key in dictionary:
    print(key, dictionary[key], sep=": ")


def guess(Key, Value):
    if Key in dictionary.keys() and Value == dictionary[Key]:
        return True
    else:
        return False

print(guess("Artist", "Depeche Mode"))
