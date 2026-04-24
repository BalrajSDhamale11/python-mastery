# 🔺 Level 2 — Logic Challenge
# "The Input Validator"

# (1.) The Beginner Method (Code duplication occurs here)
"""
number = int(input("Enter a number between 1 and 10: "))

while number < 1 or number > 10:
    print("❌ Invalid! Please enter between 1 and 10.")
    number = int(input("Enter a number between 1 and 10: "))

print(f"✅ Valid input received: {number}")

"""
# (2.) Professional Input Validation Pattern (Standard, No code duplication)

while True:
    number = int(input("Enter a number between 1 and 10: "))
    if 1 <= number <= 10: # 
        break
    print("❌ Invalid! Please enter between 1 and 10.")

print(f"✅ Valid input received: {number}")


# NOTE :
# If you can use this condition (if number < 1 or number > 10:) in Professional method
"""
while True:
    number = int(input("Enter a number between 1 and 10: "))
    
    if number < 1 or number > 10:
        print("❌ Invalid! Please enter between 1 and 10.")
    else:
        break # The number is good, so stop the loop

print(f"✅ Valid input received: {number}")

"""