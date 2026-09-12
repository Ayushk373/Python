import random

# Pick a secret number between 1 and 10
secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("Correct! You won.")
else:
    print("Wrong! The number was:", secret_number)
