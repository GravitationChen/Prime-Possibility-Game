# Author: Andy Boyu Chen
# Last Modified Date: Nov 11, 2023
# Version: 1.0.0
# Description: This program is a game that allows the user to roll n digits and try to make prime numbers.

# Import tkinter and random module
import tkinter as tk
import random

# Class: PossibilityGame: Responsible for the game logic and GUI
class PossibilityGame:
    # Function: __init__: initializes the game
    def __init__(self, root):
        self.root = root
        self.root.title("Possibility Game")

        self.player_score = 0
        self.computer_score = 0
        self.digit_choices = list(range(1, 7))
        self.selected_digits = tk.IntVar(value=1)

        self.label = tk.Label(root, text="Roll some digits and try to make prime numbers!")
        self.label.pack()

        self.player_score_label = tk.Label(root, text="Player: 0")
        self.player_score_label.pack()

        self.computer_score_label = tk.Label(root, text="Computer: 0")
        self.computer_score_label.pack()

        self.digit_label = tk.Label(root, text="Select the number of digits to roll:")
        self.digit_label.pack()

        self.digit_menu = tk.OptionMenu(root, self.selected_digits, *self.digit_choices)
        self.digit_menu.pack()

        self.rolled_digits_label = tk.Label(root, text="Rolled Digits:")
        self.rolled_digits_label.pack()

        self.roll_button = tk.Button(root, text="Roll Digits", command=self.roll_digits)
        self.roll_button.pack()

        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game)
        self.reset_button.pack()

        self.game_over = False

    # Function: is_prime: checks if a number is prime
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Function: roll_digits: rolls n digits and checks if the number is prime
    def roll_digits(self):
        if self.game_over:
            return

        num_of_digits = self.selected_digits.get()
        digits = [str(random.randint(0, 9)) for _ in range(num_of_digits)]
        rolled_digits = "".join(digits)
        self.rolled_digits_label.config(text=f"Rolled Digits: {rolled_digits}")
        number = int(rolled_digits)
        if self.is_prime(number):
            self.player_score += num_of_digits
        else:
            self.computer_score += 1
        self.update_scores()

        if abs(self.player_score - self.computer_score) >= 5:
            self.end_game()

    # Function: update_scores: updates the player and computer scores
    def update_scores(self):
        self.player_score_label.config(text=f"Player: {self.player_score}")
        self.computer_score_label.config(text=f"Computer: {self.computer_score}")

    # Function: end_game: ends the game and displays the winner
    def end_game(self):
        self.roll_button.config(state=tk.DISABLED)
        self.game_over = True
        if self.player_score > self.computer_score:
            self.label.config(text="Congratulations! You win!")
        elif self.player_score < self.computer_score:
            self.label.config(text="Computer wins. Better luck next time!")
        else:
            self.label.config(text="It's a tie!")

    # Function: reset_game: resets the game
    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.player_score_label.config(text="Player: 0")
        self.computer_score_label.config(text="Computer: 0")
        self.rolled_digits_label.config(text="Rolled Digits:")
        self.roll_button.config(state=tk.NORMAL)
        self.label.config(text="Roll some digits and try to make prime numbers!")
        self.game_over = False

# Runs the game
if __name__ == "__main__":
    root = tk.Tk()
    game = PossibilityGame(root)
    root.mainloop()
