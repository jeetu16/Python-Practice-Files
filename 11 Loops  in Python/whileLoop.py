# while loop = perform some code WHILE some condition remains true

# ---> Exercise 1
'''
name = input("Enter your name: ")

while name =="":
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"Hello,{name}")
'''

# ---> Exercise 2
'''
age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))
print(f"You are {age} years old")
'''

# ---> Exercise 3
'''
food = input("Enter a food you like (q to quit): ")

while not food == 'q':
    print(f"You like {food}")
    food = input("Enter another food you like(q to quit): ")
print("Bye")
'''

# ---> Exercise 4

num = int(input("Enter a number between 1 to 10: "))

while num < 1 or num > 10:
    print(f'{num} is not valid')
    num = int(input("Enter a number between 1 to 10: "))
print(f"You picked the number {num}")

