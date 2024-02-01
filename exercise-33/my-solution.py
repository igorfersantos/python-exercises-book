def commaFormat(number) -> str:
    number = str(number)

    if len(number) < 4: return number

    precision_point_numbers = ''
    if '.' in number:
        precision_point_numbers = number[number.index('.'):]
        number = number[0:number.index('.')]

    triplet = ''
    comma_number = ''
    for i in range(len(number) - 1, -1, -1):
        if len(triplet) == 3:
            comma_number = triplet + ',' + comma_number
            triplet = ''
        triplet = number[i] + triplet
    
    comma_number = triplet + ',' + comma_number[:-1]

    return comma_number + precision_point_numbers

assert commaFormat(1) == '1'
assert commaFormat(10) == '10'
assert commaFormat(100) == '100'
assert commaFormat(1000) == '1,000'
assert commaFormat(10000) == '10,000'
assert commaFormat(100000) == '100,000'
assert commaFormat(1000000) == '1,000,000'
assert commaFormat(1234567890) == '1,234,567,890'
assert commaFormat(1000.123456) == '1,000.123456'
print('worked!')