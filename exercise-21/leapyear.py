def isLeapYear(year):
  is_divisible_by_four = year % 4 == 0
  is_divisible_by_one_hundred = year % 100 == 0
  is_divisible_by_four_hundred = year % 400 == 0
  is_leap_year = False

  if is_divisible_by_four:
    is_leap_year = True

  if is_divisible_by_one_hundred:
    is_leap_year = False

  if is_divisible_by_four_hundred:
    is_leap_year = True
  
  return is_leap_year