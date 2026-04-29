#🔺 Level 3 — Full Integration
# "The Pattern Printer + Prime Checker"

""" (1). Part A — Pattern Printer: """
n = int(input("Enter a number: "))
print()
# Method (a) Right Triangle
for i in range(1, n+1):       # Outer loop: Handles the number of rows
    for j in range(i):        # Inner loop: Handles the number of stars per row
        print("*", end = " ") # print star and space without a newline
    print()                   # Move to the next line after each row

# Method (b) Right Triangle
"""
for i in range(1, n+1):
   print(i * "*" " ") 

"""
# Inverted Right Triangle
"""
for i in range(n, 0, -1):
    print("* " * i)

"""

""" (2). Part B — Prime Checker: """
print("==============================================")

limit = int(input("Enter a number to check primes up to: "))
print(f"\nPrime numbers from 2 to {limit}: ")
prime_counter = 0

for num in range(2, limit + 1):
    for i in range(2, num): 
    # Optimized version
    # for i in range(2, int(num**0.5) + 1):  # only checks up to square root
        if (num % i) == 0:
            break
    else:
        print(num, end = " ")
        prime_counter += 1


print(f"\n\nTotal primes found: {prime_counter}")