# 🔺 Level 2 — Logic Challenge
# "The Strict Calculator"

number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))

addition = number_1 + number_2
difference = number_1 - number_2
product = number_1 * number_2

print(f"Sum        : {addition}")
print(f"Difference : {difference}")
print(f"Product    : {product}")

if number_2 == 0:
    print("Error! Cannot divide by 0")
else:
     division = number_1 / number_2 #we can use '//' just to get only integer part
     print(f"Division   : {division}")