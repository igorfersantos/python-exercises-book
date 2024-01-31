def writeToFile(filename, text):
  try:
    with open(filename, 'w') as file:
      file.write(text)
  finally:
    file.close()


def appendToFile(filename, text):
  try:
    with open(filename, 'a') as file:
      file.write(text)
  finally:
    file.close()


def readFromFile(filename):
  try:
    with open(filename, 'r') as file:
      return file.read()
  finally:
    file.close()

writeToFile('greet.txt', 'Hello!\n')

appendToFile('greet.txt', 'Goodbye!\n')

print(readFromFile('greet.txt'))
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'