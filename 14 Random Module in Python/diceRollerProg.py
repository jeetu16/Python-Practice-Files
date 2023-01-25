import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}


while True:
    print("-------------------------------------------------------")
    dice = []

    total = 0

    num_of_dice = int(input("How many dice you want to roll? :"))

    for die in range(num_of_dice):
        dice.append(random.randint(1, 6))

    print()
    print(f"{num_of_dice} dice after roll ")

    for num in range(5):
        for die in dice:
            print(dice_art.get(die)[num], end="")
        print()

    for num in dice:
        total += num
    print(f"Total is {total}")

    temp = input("Do you want to exit? (Y/N): ").lower()
    if temp == 'y':
        break
    else:
        continue
