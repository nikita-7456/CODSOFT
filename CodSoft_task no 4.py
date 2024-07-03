import random
options = ["Rock", "Paper", "Scissor"]


def RockPaperScissor():
    b = "y"
    user_score = 0
    computer_score = 0
    while b == "y":
        print("ROCK PAPER SCISSOR GAME")
        print("Choose from the following by entering the number next to them: ")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissor")
        user_input = int(input("Enter you choice:"))
        comp = random.randint(0, 2)
        computer_choice = options[comp]
        user_choice = options[user_input - 1]
        print("Your choice: ", user_choice)
        print("Computer's choice: ", computer_choice)
        if (user_choice == "Rock") and (computer_choice == "Rock"):
            pass
        elif (user_choice == "Rock") and (computer_choice == "Paper"):
            computer_score += 1
        elif (user_choice == "Rock") and (computer_choice == "Scissor"):
            user_score += 1
        elif (user_choice == "Paper") and (computer_choice == "Rock"):
            user_score += 1
        elif (user_choice == "Paper") and (computer_choice == "Paper"):
            computer_score += 0
        elif (user_choice == "Paper") and (computer_choice == "Scissor"):
            computer_score += 1
        elif (user_choice == "Scissor") and (computer_choice == "Rock"):
            computer_score += 1
        elif (user_choice == "Scissor") and (computer_choice == "Paper"):
            computer_score += 1
        elif (user_choice == "Scissor") and (computer_choice == "Scissor"):
            computer_score += 1
        print("USER SCORE: ", user_score)
        print("COMPUTER SCORE: ", computer_score)
        cont = input("Do you want to continue the game (y/n): ")
        if cont == "n":
            b = False
            if user_score > computer_score:
                print("Winner: You!")
            elif computer_score > user_score:
                print("Winner: Computer")
            elif computer_score == user_score:
                print("It's a tie!")
        elif cont == "y":
            pass
        else:
            print("Invalid entry")

RockPaperScissor()



