# logical operators = used on conditional statements

#              and = checks two or more conditions are True
#               or = checks if at least one condition is True
#              not = True if condition is False, and vice versa

# ---> and operator
'''
age = 14
votorId = "Yes"
if age >= 18 and votorId == "Yes":
    print("You can vote")
else:
    print("You must be 18 or older and have voterId card")
'''

# ---> or operator

money = "no"
age = 18
if age >= 18 or money == "Yes":
    print("You can go into the PUB")
else:
    print("You can't go anymore into the PUB")


# ---> not operator
'''
sunny = True
if not sunny:
    print("It is cloudy")
else:
    print("It is sunny")
'''