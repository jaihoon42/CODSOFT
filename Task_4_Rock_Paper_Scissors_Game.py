
# Rock-Paper-Scissors Game


import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def main():
    print("Welcome to Rock-Paper-Scissors!")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user_choice == "quit":
            break
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = get_winner(user_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score -> You: {user_score}, Computer: {computer_score}")
        print("-" * 30)

    print("Thanks for playing!")
    print(f"Final Score -> You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    main()