# 1. Define a set that contains tuples. Each tuple should contain two strings:
# i. The name of an artist
# ii. A song by that artist

# Example set
# songs = {
#     ('Nickelback', 'How You Remind Me'), 
#     ('Will.i.am', 'That Power'),
#     ('Miles Davis', 'Stella by Starlight'),
#     ('Nickelback', 'Animals')
# }

songs = {
  ('Nickelback', 'Photograph'),
  ('Nickelback', 'How You Remind Me'),
  ('TheStokes', 'Someday'),
  ('TheBeatles', 'For you blue')
}

# 2. Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.

anythingElse = {band for band in songs if band[0] != 'Nickelback'}
print(anythingElse)

