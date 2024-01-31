def ordinalSuffix(number):
  number_string = str(number)

  if number_string[-2:] in ('11', '12', '13'):
    return number_string + 'th'
  
  if '1' in number_string[-1:]:
    return number_string + 'st'
  
  if '2' in number_string[-1:]:
    return number_string + 'nd'
  
  if '3' in number_string[-1:]:
    return number_string + 'rd'
    
  return number_string + 'th'

assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'
print("worked!")