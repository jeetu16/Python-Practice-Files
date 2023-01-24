import random

options = ['rock','paper','scissor']
running = True

print("----------rock, paper, scissor -----------------")


while running:
    print()
    player = True 
    while player:
        computer = random.choice(options)
        player = input("Enter a choice(rock,paper,scissor): ")
        if player.lower() not in options:
            print("Please select valid Option :")
            
            continue
        else:
            print(f"Computer Choice {computer}")
            print()
            if player.lower() == computer:
                print("It's a tie")
            elif player.lower() == 'rock' and computer == 'scissors':
                print("You Win!")
            elif player.lower() == 'paper' and computer == 'rock':
                print("You Win!")
            elif player.lower() == 'scissor' and computer == 'paper':
                print("You Win!")
            else:
                print("You Lose!")
            break
        print()

    play_status = True
    while play_status:
        play_status = input("Do you want to Continue to Play? (Y/N): ").lower()
        print()
        if play_status == 'y':
            running = True
            break
        elif play_status == 'n':
            running = False
            break
        else:
            print("Please Select Valid Option")
            continue

print("Thank You for Playing")