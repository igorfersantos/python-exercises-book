def getHoursMinutesSeconds(totalSeconds):
  if not totalSeconds:
    return '0s'

  seconds = totalSeconds
  minutes = 0
  hours = 0
  days = 0

  while seconds >= 60: 
    minutes += 1
    seconds -= 60
  
  if minutes >= 60:
    while minutes >= 60: 
      hours += 1 
      minutes -= 60
  
  if hours > 24:
    while hours >= 24:
      days += 1
      hours -= 24
      
  final_string = []
  if days != 0:
    final_string.append(str(days) + 'd')
  if hours != 0:
    final_string.append(str(hours) + 'h')
  if minutes != 0:
    final_string.append(str(minutes) + 'm')
  if seconds != 0:
    final_string.append(str(seconds)  + 's')
  return ' '.join(final_string)


assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '1d 1h 42s'
assert getHoursMinutesSeconds(0) == '0s'
print('worked!')