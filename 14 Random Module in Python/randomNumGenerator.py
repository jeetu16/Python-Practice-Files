import random

low = 0
high = 100

num = random.randint(low,high)
guesses = 0

print("------------------------------")
while True:
    my_guess = int(input(f"Guess a Number between {low} - {high}: "))
    guesses += 1

    if my_guess < num :
        print(f"{my_guess} is too low.")
    elif my_guess > num :
        print(f'{my_guess} is too high')
    else:
        print(f"Your guess {my_guess} is right! ")
        break

print("------------------------------")

print(f"This round took you {guesses} guesses")