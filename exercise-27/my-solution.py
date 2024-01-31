def drawRectangle(width, height):
  if width <= 0 or height <= 0: return

  for y in range(height):
    for x in range(width):
      print('#', end='')
    print('')

drawRectangle(10, 4)