# 📝 Your Problem — Level 1
# "The Multiplication Table"

number = int(input("Enter a number: "))

print(f"\n===== Multiplication Table of {number} =====")
for i in range(1,11):
    print(f"{number} x {i} = {number * i}")

print("======================================")