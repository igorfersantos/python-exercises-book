def getChessSquareColor(column, row):
  if column < 0 or column > 7:
    return ''
  if row < 0 or row > 7:
    return ''

  if (column + row) % 2 == 0:
    return 'white'
  return 'black'


assert getChessSquareColor(0, 0) == 'white'

assert getChessSquareColor(1, 0) == 'black'

assert getChessSquareColor(0, 1) == 'black'

assert getChessSquareColor(7, 7) == 'white'

assert getChessSquareColor(6, 7) == 'black'

assert getChessSquareColor(0, 8) == ''

assert getChessSquareColor(2, 9) == ''

print('worked!')