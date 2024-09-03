import random
user_wins=0
computer_wins=0
options=["rock", "paper", "scissors"]
while True:
    user_input=input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input=="q":
        break
    elif user_input not in options:
        print("Not Valide Please type again")
        continue
    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print("Computer picked", computer_pick+".")
    if user_input=="rock" and computer_pick=="scissors":
        print("You won!")
        user_wins+=1
    elif user_input=="scissors" and computer_pick=="paper":
        print("You won!")
        user_wins+=1
    elif user_input=="papers" and computer_pick=="rock":
        print("You won!")
        user_wins+=1
    elif user_input==computer_pick:
        print("Tied")
    else:
        print("You lost")
        computer_wins+=1
if computer_wins>user_wins:
    print("You have lost the game as computer has", computer_wins,"wins and you have", user_wins,"wins")
else:
    print("You have won the game as computer has only",computer_wins,"wins and you have", user_wins,"wins")
