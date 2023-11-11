rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
# Function to get the user's choice and print the corresponding ASCII art.
def get_user_choice():
    print("What do you choose?")
    input_choice = input("Type 'rock', 'paper' or 'scissors': ").lower()

    if input_choice == "rock":
        print(rock)
    elif input_choice == "paper":
        print(paper)
    elif input_choice == "scissors":
        print(scissors)
    else:
        print("Invalid choice. Please type 'rock', 'paper', or 'scissors'.")
        return None  # Return None to indicate an invalid choice

    return input_choice

# Function to get the computer's choice and print the corresponding ASCII art.
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    comp_choice = random.choice(choices)

    print(f"Computer chose:\n{comp_choice}")
    if comp_choice == "rock":
        print(rock)
    elif comp_choice == "paper":
        print(paper)
    elif comp_choice == "scissors":
        print(scissors)

    return comp_choice

# Function to determine the winner of the game.
def play_game(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a tie"
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissors" and comp_choice == "paper"):
        return "You win!"
    else:
        return "You lose"

# Main game logic.
print("Welcome to Rock, Paper, Scissors!")
user_choice = get_user_choice()  # Get the user's choice
if user_choice:  # If user_choice is not None (i.e., the user made a valid choice)
    comp_choice = get_computer_choice()  # Get the computer's choice
    result = play_game(user_choice, comp_choice)  # Determine the game result
    print(result)  # Print the game result
