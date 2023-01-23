menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

my_food = []

total = 0

print("----------- MENU ------------")
for key,value in menu.items():
    print(f'{key:10}: ${value:.2f}')

print("-----------------------------")

while True:
    food  = input("What would like to eat? (q for quit): ").lower()
    if food == 'q':
        break
    elif food not in menu.keys():
        continue
    else:
        my_food.append(food)

print("-----------Your Cart-------------")
for f in my_food:
    total += menu.get(f)
    print(f"{f:10} ${menu.get(f):.2f}")

print("---------------------------------")

print(f"Your total is ${total:.2f}")



