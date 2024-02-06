def reverseString(text):
    if len(text) == 0: return ''
    text = list(text)

    reversed_string = ''
    for c in range(len(text)-1, -1, -1):
        reversed_string+=text[c]
    return reversed_string

assert reverseString('Hello') == 'olleH'

assert reverseString('') == ''

assert reverseString('aaazzz') == 'zzzaaa'

assert reverseString('xxxx') == 'xxxx'

print('worked!')