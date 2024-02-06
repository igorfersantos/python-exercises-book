COINS = {"quarters": 25, "dimes": 10, "nickels": 5, "pennies": 1}
def makeChange(amount):
    count = {"quarters": 0, "dimes": 0, "nickels": 0, "pennies": 0}

    for coin in count.keys():
        coin_amount = amount // COINS[coin]
        if coin_amount != 0:
            count[coin] += coin_amount
            amount -= COINS[coin] * coin_amount
    
    final_count = {}
    for c in count.keys():
        if count[c] != 0:
            final_count[c] = count[c]

    return final_count
    

assert makeChange(30) == {'quarters': 1, 'nickels': 1}

assert makeChange(10) == {'dimes': 1}

assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}

assert makeChange(100) == {'quarters': 4}

assert makeChange(125) == {'quarters': 5}