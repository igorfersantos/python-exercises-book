def mode(numbers):
  if len(numbers) == 0: return None
  mode = {}

  for num in numbers:
    if num not in mode:
       mode[num] = 0
       continue
    mode[num] += 1

  greatest_apparence = next(iter(mode.keys()))
  for key in mode:
    if mode[key] > mode[greatest_apparence]:
      greatest_apparence = key
  return greatest_apparence   

assert mode([]) == None

assert mode([1, 2, 3, 4, 4]) == 4

assert mode([1, 1, 2, 3, 4]) == 1

import random

random.seed(42)

testData = [1, 2, 3, 4, 4]

for i in range(1000):

    random.shuffle(testData)

    assert mode(testData) == 4

print('worked!')