import random
target = random.randint(1, 50)
guess = None
while guess != target:
    guess = int(input("Guess a number between 1 and 50: "))
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
print("Correct! You guessed the number.")