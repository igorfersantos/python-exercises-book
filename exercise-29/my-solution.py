def drawPyramid(height):
  count = height
  for i in range(1, height * 2, 2):
    print(('#' * i).rjust(count))
    count += 1

drawPyramid(8)
