def drawBorder(width, height):
  if width < 2 or height < 2: return
  inner_width = width - 2
  inner_height = height - 2
  print('+' + ('-'*inner_width) + '+')
  for row in range(inner_height):
    print('|' + (' '*inner_width) + '|')
  print('+' + ('-'*inner_width) + '+')

drawBorder(16,4)