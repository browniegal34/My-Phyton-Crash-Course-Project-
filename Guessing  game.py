import random

number = random.randint(1, 100)
max_attempts = 7
attempts = 0

print("Guess the number (1 - 100)")
print("You have", max_attempts, "tries")

while attempts < max_attempts:
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Enter a number!")
        continue

    attempts += 1

    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("Correct! You got it in", attempts, "tries")
        break
else:
    print("Game over. The number was", number)