# bnc.py
from random import randint

# Define roles
roles = ["Bear", "Ninja", "Cowboy"]

# Function to get the computer's random role
def get_computer_choice():
    return roles[randint(0, 2)]

# Function to compare player's and computer's choices
def determine_winner(player, computer):
    if player == computer:
        return "DRAW!"
    elif player == "Bear":
        if computer == "Ninja":
            return "You win! Bear eats Ninja."
        else:
            return "You lose! Cowboy shoots Bear."
    elif player == "Ninja":
        if computer == "Cowboy":
            return "You win! Ninja defeats Cowboy."
        else:
            return "You lose! Bear eats Ninja."
    elif player == "Cowboy":
        if computer == "Bear":
            return "You win! Cowboy shoots Bear."
        else:
            return "You lose! Ninja defeats Cowboy."
    else:
        return "Invalid choice! Please choose Bear, Ninja, or Cowboy."

# Main game loop
def play_game():
    print("Welcome to Bear, Ninja, Cowboy!")
    
    while True:
        # Get user input
        player = input("Bear, Ninja, or Cowboy? > ").capitalize()
        
        # Get random computer role
        computer = get_computer_choice()
        
        # Determine and display who wins
        result = determine_winner(player, computer)
        print(f"Computer chose: {computer}")
        print(result)
        
        # Ask the player if they want to play again
        play_again = input("Would you like to play again? (yes/no) > ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Run the game
play_game()
