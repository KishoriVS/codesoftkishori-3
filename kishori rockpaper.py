import random


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    return "computer"


def play_game():
    user_score = 0
    computer_score = 0
    while True:
        print("\nRock-Paper-Scissors Game")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")


        user_choice_index = input("Enter your choice (1/2/3/4): ")
        if user_choice_index == "4":
            break


        if user_choice_index not in ["1", "2", "3"]:
            print("Invalid choice. Please try again.")
            continue


        choices = ["rock", "paper", "scissors"]
        user_choice = choices[int(user_choice_index) - 1]
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)


        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")


        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1


        print(f"Score - You: {user_score}, Computer: {computer_score}")
        play_again = input("\nPlay again? (y/n): ")
        if play_again.lower() != "y":
            break


if __name__ == "__main__":
    play_game()

        



            
