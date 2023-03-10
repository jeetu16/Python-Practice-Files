import math


# ---> Arithmatic Operations 
"""
friend = 10

# friend = friend + 1   # Addition(+) operator
# friend += 1           # Augmented Assignment Operator

# friend = friend - 2   # Subtraction(-) operator
# friend -= 2           # Augmented Assignment Operator

# friend = friend * 3   # Multiplication(*) operator
# friend *= 3           # Augmented Assignment Operator

# friend = friend / 2   # Division(/) operator
# friend /= 2           # Augmented Assignment Operator

# friend = friend**2    # exponent Operator
# friend **= 2          # Augmented Assignment Operator

# friend = friend % 3   # Modulus(%) operator
# friend %= 3           # Augmented Assignment Operator

print(f"You have {friend} friend")
"""


# ---> Built In Math Functions
"""
x = 3.23
y = 40
z = -20

# result = round(3)           # round(value,optional)
# result = abs(z)             # 20
# result = pow(4,3)           # 64
# result = max(x,y,z)         # 40
# result = min(x,y,z)         # -20
print(f"Result is: {result}")
"""


# ---> Contant Values in Python
'''
constant = math.pi          # 3.141592653589793
constant = math.e           # 2.718281828459045
print(f"Contant value:{constant}")
'''


# ---> other math function in python 
'''
answer = math.sqrt(5)       # 2.23606797749979
answer = math.ceil(9.12)    # 10
answer = math.floor(9.95)   # 9
print(f"Answer :{answer}")
'''


# ---> Exercise 1 : Circumference of circle
""""
radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference of Circle is: {round(circumference,2)}cm")
"""


# ---> Exercise 2 : Area of cicle
'''
radius = float(input("Enter the radius of a cirlce: "))
area = math.pi * pow(radius,2)
print(f"The area of the Circle is: {round(area,2)}cm^2")
'''


# ---> Exercise 3 : Hypotenuse of right angle triangle

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a,2)+pow(b,2))

print(f"Side C : {c}")