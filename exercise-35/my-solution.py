def getTitleCase(text: str):
    if len(text) == 0: return ''
    
    text = list(text)
    words = []

    word = ''
    for i, c in enumerate(text):
        if c.isalpha():
            word += c
        else:
            words.append(word + c)
            word = ''
    words.append(word)

    text = ''
    for x, word in enumerate(words):
        for y, c in enumerate(word):
            if y == 0: 
                text+= words[x][y].upper()
            else:
                text+= words[x][y].lower()
    
    return text

assert getTitleCase('Hello, world!') == 'Hello, World!'
assert getTitleCase('HELLO') == 'Hello'
assert getTitleCase('hello') == 'Hello'
assert getTitleCase('hElLo') == 'Hello'
assert getTitleCase('') == ''
assert getTitleCase('abc123xyz') == 'Abc123Xyz'
assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'
assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'
import random
random.seed(42)
chars = list('abcdefghijklmnopqrstuvwxyz1234567890 ,.')
for i in range(1000):
    random.shuffle(chars)
    assert getTitleCase(''.join(chars)) == ''.join(chars).title()

print('worked!')