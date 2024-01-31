def fizzBuzz(upTo):
  for number in range(1, upTo + 1):
    fizzBuzz = ""
    if number % 3 == 0:
      fizzBuzz += "Fizz"
    if number % 5 == 0:
      fizzBuzz += "Buzz"

    if fizzBuzz:
      print(fizzBuzz, end=" ")
    else:
      print(number, end=" ")
  print('\n')


assert fizzBuzz(35) == "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz"