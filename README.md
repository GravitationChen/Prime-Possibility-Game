# Possibility Game Documentation
## Introduction
The Possibility Game is a simple text-based game implemented in Python with a graphical user interface (GUI) using the Tkinter library. The game's objective is to roll a sequence of digits and attempt to form prime numbers to score points. The first player to achieve a lead of 5 points wins the game.

## Features
The game offers the following features:

Rolling Digits: The player can choose the number of digits to roll, ranging from 1 to 6 digits.

Scoring: The player scores points when they roll a sequence of digits that forms a prime number. The number of points earned is based on the number of digits used.

Game Progress: The player's and computer's scores are displayed in the GUI, and the game continues until one player achieves a lead of 5 points or more.

Reset Button: After the game concludes, the player can reset the game to start a new round.

## How to Play
Select the number of digits to roll by using the dropdown menu labeled "Select the number of digits to roll."

Click the "Roll Digits" button to generate a sequence of digits according to your selection.

The rolled digits are displayed in the "Rolled Digits" label.

If the sequence of digits forms a prime number, you earn points based on the number of digits rolled.

The game continues until one player has a lead of 5 points or more.

To start a new game, click the "Reset Game" button.

## Probability
The game's probabilities for winning a round are calculated as follows:

### Rolling a 1-digit prime number:
Prime numbers between 0 and 9 are 2, 3, 5, and 7. There are 4 prime numbers in this range.

The total number of choices in the range from 0 to 9 is 10 (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9).

So, the probability of randomly selecting a prime number in this range is:

Number of prime numbers / Total number of choices = 4/10 = 2/5

Therefore, the probability is 2/5 or 40%.

### Rolling a 2-digit prime number:
Prime numbers between 0 and 99 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, and 97. There are 25 prime numbers in this range.

The total number of choices in the range from 0 to 99 is 100 (0 to 99, inclusive).

So, the probability of randomly selecting a prime number in this range is:

Number of prime numbers / Total number of choices = 25/100 = 1/4

Therefore, the probability is 1/4 or 25%.

### Rolling a 3-digits prime number:
Prime numbers between 0 and 999 can be found by using a prime number sieve or a list of prime numbers. There are 168 prime numbers in this range.

The total number of choices in the range from 0 to 999 is 1000 (0 to 999, inclusive).

So, the probability of randomly selecting a prime number in this range is:

Number of prime numbers / Total number of choices = 168/1000 = 42/250 = 21/125

Therefore, the probability is 21/125 or approximately 16.8%.

### Rolling a 4-digit prime number:
Prime numbers between 0 and 9999 can be found by using a prime number sieve or a list of prime numbers. There are 1229 prime numbers in this range.

The total number of choices in the range from 0 to 9999 is 10000 (0 to 9999, inclusive).

So, the probability of randomly selecting a prime number in this range is:

Number of prime numbers / Total number of choices = 1229/10000

This is an exact fraction, and if you'd like it in decimal form, you can calculate it:

1229 / 10000 ≈ 0.1229

Therefore, the probability is approximately 12.29%.

### Rolling a 5-digit prime number:
Prime numbers between 0 and 99999 can be found by using a prime number sieve or a list of prime numbers. There are 9592 prime numbers in this range.

The total number of choices in the range from 0 to 99999 is 100000 (0 to 99999, inclusive).

So, the probability of randomly selecting a prime number in this range is:

Number of prime numbers / Total number of choices = 9592/100000

This is an exact fraction, and if you'd like it in decimal form, you can calculate it:

9592 / 100000 ≈ 0.09592

Therefore, the probability is approximately 9.592%.

### Rolling a 6-digit prime number:
Prime numbers between 0 and 999999 can be found by using a prime number sieve or a list of prime numbers. There are 78498 prime numbers in this range.

The total number of choices in the range from 0 to 999999 is 1000000 (0 to 999999, inclusive).

So, the probability of randomly selecting a prime number in this range is:

Number of prime numbers / Total number of choices = 78498/1000000

This is an exact fraction, and if you'd like it in decimal form, you can calculate it:

78498 / 1000000 ≈ 0.078498

Therefore, the probability is approximately 7.8498%.

### Important Note
These probabilities assume that the game adheres to the prime number rule and that the distribution of digits in each roll is random.

## Conclusion
The Possibility Game is an entertaining and educational game that challenges the player's understanding of prime numbers and probability. It can be used for fun or as an educational tool to explore the concept of prime numbers and chance. The program's simple interface makes it accessible to players of all ages.