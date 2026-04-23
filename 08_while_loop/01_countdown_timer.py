# 📝 Your Problem — Level 1
# "The Countdown Timer"

# --- APPROACH 1: THE Beginner / DESTRUCTIVE METHOD ---
# This method is shorter but "consumes" the original variable.
starting_number = int(input("Enter starting number: "))
count = 1

while starting_number >= count:
    print(starting_number)
    starting_number -= 1  # The original value is changed/lost here

print("🚀 Blastoff!")
# Note: After this loop, starting_number is 0. 
# You cannot easily reuse the 'input value' without resetting it manually.

# --- APPROACH 2: THE PRESERVATIVE METHOD ---
# This method uses a temporary 'count' variable to keep the original input safe.
"""
starting_number = int(input("\nEnter starting number again: "))
count = starting_number

while count >= 1:
    print(count)
    count -= 1  

print("🚀 Blastoff!")
# Note: After this loop, starting_number is still its original value.
# You can still use it for other calculations later.

"""