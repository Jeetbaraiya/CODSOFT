import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("Choose rock, paper, or scissors: ").strip().lower()
        if user_input in choices:
            return user_input
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (
        (user == 'rock' and computer == 'scissors') or
        (user == 'scissors' and computer == 'paper') or
        (user == 'paper' and computer == 'rock')
    ):
        return 'user'
    else:
        return 'computer'

def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_score = 0
    computer_score = 0
    round_num = 1
    while True:
        print(f"\n--- Round {round_num} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        winner = determine_winner(user_choice, computer_choice)
        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'user':
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        print(f"Score -> You: {user_score} | Computer: {computer_score}")
        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again not in ('yes', 'y'):
            print("\nThanks for playing!")
            print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
            break
        round_num += 1

if __name__ == "__main__":
    main() 