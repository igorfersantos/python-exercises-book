def drawBox(size):
  if size < 1:
    return
  
  left_spaces = size + 1
  interior_size_spaces = size - 1
  print((' ' * left_spaces) + '+' + ('-'*(size*2)) + '+')
  for vertical_line in range(size):
    left_spaces -= 1
    left_string = ' ' * left_spaces
    middle_string = '/' + (' ' * (size*2)) + '/'
    right_string = (' ' * vertical_line) + "|" 
    print(left_string+middle_string+right_string)
  print('+' + ('-'*(size*2)) + '+' + (' ' * size) + '+')
  for vertical_line in range(size, 0, -1):
    middle_string = '|' + (' ' *(size*2)) + '|'
    right_string = (' ' * (vertical_line - 1)) + "/" 
    print(middle_string+right_string)
  print('+' + ('-'*(size*2)) + '+')

for i in range(1, 6):
    drawBox(i)