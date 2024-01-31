def median(numbers: list):
  if not numbers: return None
  numbers = sorted(numbers)

  if len(numbers) % 2 == 0:
    middle_number_pos = int(len(numbers)/2) - 1
    middle_most_numbers = numbers[middle_number_pos] + numbers[middle_number_pos+1]
    return middle_most_numbers / 2
  
  return numbers[int(len(numbers)/2)]

assert median([]) == None

assert median([1, 2, 3]) == 2

assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5

assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6

import random

random.seed(42)

testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]

for i in range(1000):

    random.shuffle(testData)

    assert median(testData) == 6
  
print('worked!')