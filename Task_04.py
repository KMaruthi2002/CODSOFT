import random

def get_user_choice():
    """
    Prompt the user to choose rock, paper, or scissors.
    """
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid input. Please enter rock, paper, or scissors.")

def get_computer_choice():
    """
    Generate a random choice (rock, paper, or scissors) for the computer.
    """
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner based on the user's choice and the computer's choice.
    """
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "User wins"
    else:
        return "Computer wins"

def play_game():
    """
    Play a single round of Rock, Paper, Scissors.
    """
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    print(f"User choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")
    print(f"Result: {winner}")

def play_again():
    """
    Ask the user if they want to play another round.
    """
    while True:
        response = input("Do you want to play again? (yes/no): ").lower()
        if response in ["yes", "no"]:
            return response == "yes"
        else:
            print("Invalid input. Please enter yes or no.")

def main():
    """
    Main function to play multiple rounds of Rock, Paper, Scissors.
    """
    user_score = 0
    computer_score = 0
    while True:
        play_game()
        if determine_winner(get_user_choice(), get_computer_choice()) == "User wins":
            user_score += 1
        elif determine_winner(get_user_choice(), get_computer_choice()) == "Computer wins":
            computer_score += 1
        print(f"Score: User {user_score}, Computer {computer_score}")
        if not play_again():
            break

if __name__ == "__main__":
    main()
