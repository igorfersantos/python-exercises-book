print("  | 1  2  3  4  5  6  7  8  9 10")
print("--+------------------------------")
for x in range(1, 11):
  print(str(x).rjust(2) + "|", end='')
  for y in range(1, 11):
    print(str(x*y).rjust(2), end=' ')
  print('')

