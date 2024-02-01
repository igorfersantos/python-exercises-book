DIGITS_STR_TO_INT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def convertStrToInt(stringNum: str):
    if stringNum == '0': return 0
    integerNum = 0
    
    is_negative = stringNum[0] == '-'
    if is_negative:
        stringNum = stringNum[1:]

    for i in range(len(stringNum)):
        integerNum = (integerNum * 10) + DIGITS_STR_TO_INT[stringNum[i]]

    return integerNum * -1 if is_negative else integerNum
       

for i in range(-10000, 10000):
    assert convertStrToInt(str(i)) == i
    print(f'✅ convertStrToInt(str({i}))')
print('✅✅✅✅ worked!')