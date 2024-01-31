def getSmallest(numbers: list):
  if not numbers: return None

  smallest_number = numbers[0]

  for number in numbers:
    if number < smallest_number:
      smallest_number = number
  
  return smallest_number

def getBiggest(numbers: list):
  if not numbers: return None

  biggest_number = numbers[0]

  for number in numbers:
    if number > biggest_number:
      biggest_number = number
  
  return biggest_number

assert getSmallest([1, 2, 3]) == 1
assert getSmallest([3, 2, 1]) == 1
assert getSmallest([28, 25, 42, 2, 28]) == 2
assert getSmallest([1]) == 1
assert getSmallest([]) == None
assert getBiggest([1, 2, 3]) == 3
assert getBiggest([3, 2, 1]) == 3
assert getBiggest([28, 25, 42, 2, 28]) == 42
assert getBiggest([1]) == 1
assert getBiggest([]) == None
print('worked!')