import random

print("🎲 Number Guessing Game 🎲")
number = random.randint(1, 50)
attempts = 0

while True:
    try:
        guess = int(input("Guess a number (1-50): "))
        attempts += 1
        if guess < number:
            print("Too Low ⬇️")
        elif guess > number:
            print("Too High ⬆️")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break
    except:
        print("Enter a valid number ❌")
