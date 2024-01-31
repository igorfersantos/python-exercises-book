DIGITS_INT_TO_STR = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
def convertIntToStr(integerNum):
        if integerNum == 0: return '0'
        
        is_negative = False
        if integerNum < 0:
              is_negative = True
              integerNum = abs(integerNum)
        
        stringNum = ''
        onesPlaceDigit = integerNum // 10
        while (integerNum != 0):
            stringNum = DIGITS_INT_TO_STR[integerNum - (onesPlaceDigit * 10)] + stringNum
            integerNum = integerNum // 10
            onesPlaceDigit = integerNum // 10
        
        return '-' + stringNum if is_negative else stringNum

for i in range(-10000, 10000):
    assert convertIntToStr(i) == str(i)
    print(f'✅ convertIntToStr({i})')
print('worked!')