import random

while True:
    user_action = input("Enter a choice(rock, paper, scissors): ")
    possible_action = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_action)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action==computer_action:
        print(f"Both players selected {user_action}. Its a tie! ")
    elif user_action == "rocks":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
                print("Paper covers rock! You lose!")
    elif user_action == "paper":
        if computer_action == "rock":
             print("Paper covers rock! You win!")
        else:
                print("Scissors cut paper! You lose!")
    elif user_action == "scissors":
        if computer_action == "paer":
             print("Scissors cut paper! You win!")
        else:
                print("Rock smashes scissors! You lose!")

    play_again:input("Play again?(y/n) :") # type: ignore
    if play_again !="y":
         break
    