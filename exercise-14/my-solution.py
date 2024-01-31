def average(numbers: list):
  if not numbers: return None

  sum_numbers = 0
  for num in numbers:
     sum_numbers += num

  return sum_numbers / len(numbers)

assert average([1, 2, 3]) == 2

assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2

assert average([12, 20, 37]) == 23

assert average([0, 0, 0, 0, 0]) == 0

import random

random.seed(42)

testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]

for i in range(1000):

    random.shuffle(testData)

    assert average(testData) == 2

print('worked!')