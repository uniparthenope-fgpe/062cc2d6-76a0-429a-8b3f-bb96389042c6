import random

number_to_guess = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input('Enter your guess: '))
    attempts += 1
    # Add your code here
