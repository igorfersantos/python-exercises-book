import leapyear

def isValidDate(year, month, day):
  if month < 1 or month > 12:
    return False
  if day < 1:
    return False
  
  is_leap_year = leapyear.isLeapYear(year)
  # February have 28 days or 29 in leap year
  if month == 2:
    if is_leap_year and day > 29:
      return False
    elif not is_leap_year and day > 28:
      return False
    return True
  # September, April, June, and November have 30 days
  if month in [4, 6, 9, 11]:
    if day > 30:
      return False
  # The rest have 31
  if day > 31:
    return False
  return True

assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False

import datetime

d = datetime.date(1970, 1, 1)

oneDay = datetime.timedelta(days=1)

for i in range(1000000):

    assert isValidDate(d.year, d.month, d.day) == True

    d += oneDay

print('Worked!')