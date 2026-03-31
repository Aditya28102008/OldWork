import random

choices = ["rock", "paper", "scissors"]

# Initialize scores
user_score = 0
computer_score = 0

while True:
    user = input("Enter rock, paper, or scissors (q to quit): ").lower()

    if user == "q":
        print("\nThanks for playing!")
        print(f"Final Score → You: {user_score} | Computer: {computer_score}")
        break

    if user not in choices:
        print("Invalid choice, try again.\n")
        continue

    computer = random.choice(choices)

    print("You:", user)
    print("Computer:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win this round!")
        user_score += 1  # Add 1 point to user
    else:
        print("Computer wins this round!")
        computer_score += 1  # Add 1 point to computer

    # Show current score
    print(f"Score → You: {user_score} | Computer: {computer_score}")
    print("-" * 30)
