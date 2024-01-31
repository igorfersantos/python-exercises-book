import random
import string

LOWER_LETTERS = string.ascii_lowercase
UPPER_LETTERS = string.ascii_uppercase
NUMBERS = string.digits
SPECIAL = '~!@#$%^&*()_+'
POSSIBLE_CHARACTERS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL
def generatePassword(length):
  if length < 12:
    length = 12
  pw = []
  pw.append(LOWER_LETTERS[random.randint(0, len(LOWER_LETTERS)-1)])
  pw.append(UPPER_LETTERS[random.randint(0, len(UPPER_LETTERS)-1)])
  pw.append(NUMBERS[random.randint(0, len(NUMBERS)-1)])
  pw.append(SPECIAL[random.randint(0, len(SPECIAL)-1)])
  length -= len(pw)
  for _ in range(length):
     pw.append(POSSIBLE_CHARACTERS[random.randint(0, len(POSSIBLE_CHARACTERS)-1)])
  random.shuffle(pw)
  return ''.join(pw)

assert len(generatePassword(8)) == 12
pw = generatePassword(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False

for character in pw:
    if character in LOWER_LETTERS:
        hasLowercase = True
    if character in UPPER_LETTERS:
        hasUppercase = True
    if character in NUMBERS:
        hasNumber = True
    if character in SPECIAL:
        hasSpecial = True
assert hasLowercase and hasUppercase and hasNumber and hasSpecial

print('worked!')
for i in range(0, 1000):
  print(generatePassword(40))