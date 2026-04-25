# 🔺 Level 3 — Full Integration
# "The Number Guessing Game"

secret_number = 13
attempts = 0

# (1). USING BREAK STATEMENT (Beginner Friendly)
while True:
    guess = int(input("Enter your guess: "))

    # Check if the guess is within the allowed range
    if 1 <= guess <= 20:
        attempts += 1  # 👈 Counts here: only for valid numbers
        if guess == secret_number:
            print(f"🎉 Correct! You got it in {attempts} attempts!")
            break      # 👈 The exit
        elif guess < secret_number:
            print("📉 Too low! Try higher.")
        else:
            print("📈 Too high! Try lower.")
    else:
         # This handles 'out of bounds' numbers without counting them
        print("Enter a valid number!")

if attempts <= 3:
    print("⭐⭐⭐ Excellent Guesser!")
elif attempts <= 6:
    print("⭐⭐ Good Guesser!")
else:
    print("⭐ Keep Practicing!")

# (2). Using CONTINUE STATEMENT (More Correct than above))
"""
secret_number = 13
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    
    # 1. THE GUARD: If the guess is bad, skip everything else
    if not (1 <= guess <= 20):
        print("❌ Enter a valid number!")
        continue  # 👈 Jumps straight back to the 'while True' line
    
    # 2. THE LOGIC: If we reach here, we KNOW the guess is 1-20
    attempts += 1 
    
    if guess == secret_number:
        print(f"🎉 Correct! You got it in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("📉 Too low! Try higher.")
    else:
        print("📈 Too high! Try lower.")

# Rating logic stays the same...
if attempts <= 3:
    print("⭐⭐⭐ Excellent Guesser!")
elif attempts <= 6:
    print("⭐⭐ Good Guesser!")
else:
    print("⭐ Keep Practicing!")
"""