import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop playing): ").lower()
    while user_choice not in choices and user_choice != 'quit':
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors (or 'quit' to stop playing): ").lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        return "win"
    else:
        return "lose"

def play_game():
    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        user_choice = get_user_choice()
        if user_choice == 'quit':
            break
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        if result == "win":
            user_score += 1
            print("You win this round!")
        elif result == "lose":
            computer_score += 1
            print("You lose this round!")
        else:
            print("It's a tie this round!")

        rounds += 1
        print(f"\nScores -> You: {user_score}, Computer: {computer_score}, Rounds played: {rounds}\n")

    print(f"Final Scores -> You: {user_score}, Computer: {computer_score}, Total rounds played: {rounds}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
