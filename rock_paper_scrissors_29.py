import random

options = ("rock", "paper", "scissors")
playing = True

while playing:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, or scissors): ").lower()

    print(f"Player: {player}\nComputer: {computer}")

    if player == computer:
        print("Tie")
    elif player == "rock" and computer == "scissors":
        print("You Win")
    elif player == "paper" and computer == "rock":
        print("You Win")
    elif player == "scissors" and computer == "paper":
        print("You Win")
    else:
        print("You Lose")

    # play_again = input("Play Again? (y/n): ").lower()
    # if play_again == 'n':
    #     playing = False

    if not input("Play again? (y/n): ").lower() == "y":
        playing = False

print("Thanks for playing")