import random

def play_game():
    user_score = 0
    computer_score = 0
    options = ["rock", "paper", "scissors"]

    print("--- Welcome to Rock, Paper, Scissors ---")
    print("Instructions: Type Rock, Paper, or Scissors to play. Type 'exit' to quit.")

    while True:
        user_choice = input("\nChoose Rock, Paper, or Scissors: ").lower()

        if user_choice == "exit":
            break

        if user_choice not in options:
            print("Invalid input. Please try again.")
            continue

        computer_choice = random.choice(options)

        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            user_score += 1
        else:
            print("You lose this round!")
            computer_score += 1

        print(f"Score - You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("\nFinal Game Results")
    print(f"Total Score - You: {user_score} | Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()