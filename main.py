##Rock,Paper,scissors Project
import tkinter as tk
from tkinter import messagebox
import random
# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return"You win!"
    else:
        return"You lose!"

# Function to handle button click
def on_button_click(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)
    messagebox.showinfo("Result", f"Computer chose:{computer_choice}\n{result}")

# Function to set up the GUI
def setup_gui():
    root = tk.Tk()
    root.title("Rock-Paper-scissors")

    label = tk.Label(root, text="Choose your option:", font=("Arial", 14))
    label.pack(pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    rock_button = tk.Button(button_frame, text="Rock", font=("Arial",12), command=lambda: on_button_click("rock"))
    paper_button = tk.Button(button_frame, text="Paper", font=("Arial",12), command=lambda: on_button_click("paper"))
    scissors_button = tk.Button(button_frame, text="scissors", font=("Arial",12), command=lambda: on_button_click("scissors"))

    rock_button.grid(row=0, column=0, padx=10)
    paper_button.grid(row=0, column=1, padx=10)
    scissors_button.grid(row=0, column=2, padx=10)

    root.mainloop()
# Main function to start the game
def main():
    setup_gui()

if __name__ == "__main__":
    main()
