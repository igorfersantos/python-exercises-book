def convertToFahrenheit(degrees_celsius: float ) -> float:
  fahrenheit_degrees = degrees_celsius * (9/5) + 32
  return fahrenheit_degrees

def convertToCelsius(degrees_fahrenheit: float ) -> float:
  celsius_degrees = (degrees_fahrenheit - 32) * (5/9)
  return celsius_degrees

assert1 = convertToCelsius(0)
assert convertToCelsius(0) == -17.77777777777778

assert convertToCelsius(180) == 82.22222222222223

assert convertToFahrenheit(0) == 32

assert convertToFahrenheit(100) == 212

assert convertToCelsius(convertToFahrenheit(15)) == 15