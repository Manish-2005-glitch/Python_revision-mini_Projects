import random

options = ("Rock", "Paper", "Scissors")
running = True

while running:
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("enter a choice :")

    print(f"Player : {player}")
    print(f"computer : {computer}")

    if player == computer:
        print("it is a tie!")
    elif player == "Rock" and computer == "Scissors":
        print("You won")
    elif player == "Paper" and computer == "Rock":
        print("you lost")
    elif player == "Scissors" and computer == "Paper":
        print("You won")
    else:
        print("you lost")
    
    if not input("wanna play again? (y/n)").lower() == "y":
        running = False

print("Thanks for playing!")


