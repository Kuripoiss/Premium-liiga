import random
while True:
    player = None
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    while player not in choices:
        player = input("Rock, paper, or scissors? ").lower()
        if player == computer:
            print("You chose: " + player)
            print("Computer chose: " + computer)
            print("It's a tie!")
        elif player == "rock":
            if computer == "paper":
                print("You chose: " + player)
                print("Computer chose: " + computer)
                print("You lose!")
            if computer == "scissors":
                print("You chose: " + player)
                print("Computer chose: " + computer)
                print("You win!")
        elif player == "paper":
            if computer == "scissors":
              print("You chose: " + player)
              print("Computer chose: " + computer)
              print("You lose!")
            if computer == "rock":
               print("You chose: " + player)
               print("Computer chose: " + computer)
               print("You win!")
        elif player == "scissors":
            if computer == "rock":
               print("You chose: " + player)
               print("Computer chose: " + computer)
               print("You lose!")
            if computer == "paper":
               print("You chose: " + player)
               print("Computer chose: " + computer)
               print("You win!")
    player_again = input("Do you wanna play again? (yes/no): ").lower()

    if player_again != "yes":
        break
print("Bye!")