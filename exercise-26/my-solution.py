def printHandshakes(people):
  handshakes = 0

  for person in range(len(people)):
    for other_person in range(person+1, len(people)):
      print("{0} shakes hands with {1}".format(people[person], people[other_person]))
      handshakes += 1
  
  return handshakes

assert printHandshakes(['Alice', 'Bob']) == 1
assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6
print('worked!')