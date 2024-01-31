def printASCIITable():
  for char in range(32, 127):
    print(f'{char} {chr(char)}')

printASCIITable()