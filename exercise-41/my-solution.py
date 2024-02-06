def rot13(text: str):
    transformed_string = ''
    for c in text:
        if not c.isalpha():
            transformed_string += c
            continue
        if c.islower():
            if ord(c) + 13 > 122:
                transformed_string += chr(ord(c) + 13 - 26)
            else:
                transformed_string += chr(ord(c) + 13)
        elif c.upper():
            if ord(c) + 13 > 90:
                transformed_string += chr(ord(c) + 13 - 26)
            else:
                transformed_string += chr(ord(c) + 13)
    return transformed_string

assert rot13('Hello, world!') == 'Uryyb, jbeyq!'

assert rot13('Uryyb, jbeyq!') == 'Hello, world!'

assert rot13(rot13('Hello, world!')) == 'Hello, world!'

assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'

assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'

print('worked!')
        