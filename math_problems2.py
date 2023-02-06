def measure_height():
    meters = float(input('Inform your height in meters: '))
    centimeters = meters * 100
    inch = 2.54 * centimeters
    feet = inch * 12
    print(f'Your height is {meters:.2f} m in Brazil. Your height in the US is around {feet:.2f}ft.')

def total_population():
    literate = 5170
    illiterate = (5170 /94)*6
    total_population = literate + illiterate
    print(total_population)

def percentage_of_black_poor():
    total = int(input('How many people?'))
    poor = total * 0.2
    black = total * 0.5
    poor_and_black = poor * 0.8
    percentage_of_black_poor = (poor_and_black *100) / black
    print(percentage_of_black_poor)

def pi():
    import math
    print(math.pi)

def calculation_with_pi():
    import math
    pi = math.pi
    calculation = pi * 14
    print(calculation)

def celsius_to_fahrenheit():
    celsius = float(input('Inform the temperature in Celsius: '))
    fahrenheit = 9 * celsius / 5 + 32
    print(fahrenheit)

def fahrenheit_to_celsius():
    fahrenheit = float(input('Inform the temperature in Fahrenheit:' ))
    celsius = (fahrenheit - 32) * 5 / 9
    print(celsius)





