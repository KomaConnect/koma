import random

while True:
    Game_options = ["rock", "paper", "scissors"]

    cpu = random.choice(Game_options)
    users_pick = input("pick either rock, paper or scissors: ")
    users = users_pick.lower()

    while users_pick not in Game_options:
        print("You picked a wrong option, try again.")
        break
        

    if users == cpu:
        print("users_pick: ", users)
        print("computer: ", cpu)
        print("it is a Tie!, try again.")

    elif users == "rock":
        if cpu == "paper":
            print("users_pick: ", users)
            print("computer: ", cpu)
            print("you lose!, play again.")

        if cpu == "scissors":
            print("users_pick: ", users)
            print("computer: ", cpu)
            print("You Win!.")

    elif users == "paper":
        if cpu == "scissors":
            print("users_pick: ", users)
            print("computer: ", cpu)
            print("you lose!, try again.")
        if cpu == "rock":
            print("users_pick: ", users)
            print("computer: ", cpu)
            print("You win!.") 

    elif users == "scissors":
        if cpu == "rock":
            print("users_pick: ", users)
            print("computer: ", cpu)
            print("you lose!, try again.")
        if cpu == "paper":
            print("users_pick: ", users)
            print("computer: ", cpu)
            print("You win!.")       

    playAgain = input("Do you want to try again? (Yes/No): ")
    playAgain = playAgain.lower()

    if playAgain != "yes":    
        break

print("Good bye, see another time.")