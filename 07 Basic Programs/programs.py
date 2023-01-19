# ---> Basic Calculator Program
'''
operator = input("Enter an operator(+ - * /):")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == '+':
    result = num1 + num2
    print(f"Result is :{round(result,3)}")
elif operator == '-':
    result = num1 - num2
    print(f"Result is :{round(result,3)}")
elif operator == '*':
    result = num1 * num2
    print(f"Result is :{round(result,3)}")
elif operator == '/':
    result = num1 / num2
    print(f"Result is :{round(result,3)}")
else :
    print(f'{operator} is not a valid operator')
'''

# ---> Weight Converter
'''
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == 'K' or unit == 'k':
    weight = weight * 2.205
    unit = 'Lbs'
    print(f"Your weight is {round(weight,2)} {unit}")
elif unit == 'L' or unit == 'l':
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is {round(weight,2)} {unit}")
else:
    print(f'{unit} was not valid unit')
'''

# ---> Temperature Converter

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")
