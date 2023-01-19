# if = Do some code IF condition is True
# else = Do something else if above condition/s are False

# ---> Exercise 1
'''
age = int(input("Enter your age:"))

if age >= 100 :
    print("You are too old to sign up")
elif age >= 18 :
    print("You are signed up now")
elif age < 0 :
    print("You haven't been born yet")
else :
    print("You must be 18+ for sign up")
'''

# ---> Exercise 2
'''
response = input("Do you want to food (Y/N)?:")

if response == "Y" or response == "y" :
    print("Have some food")
else :
    print("No food for you")
'''

# ---> Exercise 3
'''
name = input("Enter your name: ")

if name == "":
    print("You did not enter your name")
else:
    print(f'Hello, {name}')
'''

# ---> Exercise 4

online = False

if online:
    print("You are online");
else :
    print("You are offline")