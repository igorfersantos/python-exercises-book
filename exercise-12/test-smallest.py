import random, my_solution

numbers = []

for i in range(1000000):
    numbers.append(random.randint(1, 1000000000))

print('Numbers:', numbers)

print('Smallest number is', my_solution.getSmallest(numbers))