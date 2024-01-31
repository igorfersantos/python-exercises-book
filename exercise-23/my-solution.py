song = """
{0} bottles of beer on the wall,

{0} bottles of beer,

Take one down,

Pass it around,

{1} bottles of beer on the wall,
"""
count = 99

for bottles in range(count, 0, -1):
  print(song.format(bottles, bottles-1))