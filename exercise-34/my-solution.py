def getUppercase(text):
    text = list(text)
    for i, c in enumerate(text):
        if ord(c) < 97: continue
        text[i] = chr(ord(c) - 32)
    return ''.join(text)
        

assert getUppercase('Hello') == 'HELLO'
assert getUppercase('hello') == 'HELLO'
assert getUppercase('HELLO') == 'HELLO'
assert getUppercase('Hello, world!') == 'HELLO, WORLD!'
assert getUppercase('goodbye 123!') == 'GOODBYE 123!'
assert getUppercase('12345') == '12345'
assert getUppercase('') == ''