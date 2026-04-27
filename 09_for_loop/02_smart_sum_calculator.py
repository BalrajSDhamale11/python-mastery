# 🔺 Level 2 — Logic Challenge
# "The Smart Sum Calculator"

# (1). As Per The Question (With CONTINUE Statement)
n = int(input("Enter a number: "))
total_sum = 0
even_sum = 0
odd_sum = 0
total_count = 0
even_count = 0
odd_count = 0

for i in range(1, n+1):
    
    total_sum = total_sum + i
    total_count += 1 
    
    if i % 2 == 0:
        even_sum = even_sum + i
        even_count += 1
        continue # Jump to next number;

    # No 'else' needed because the 'continue' above guards this section
    odd_sum = odd_sum + i
    odd_count += 1


print(f"\n===== Summary for 1 to {n} =====")
print(f"Total Sum   : {total_sum} (count: {total_count})")
print(f"Even Sum    : {even_sum} (count: {even_count})")
print(f"Odd Sum     : {odd_sum} (count: {odd_count})")
print("================================")

# (2). Beginner Method (Without Using CONTINUE Statement)
"""
for i in range(1, n+1):
    
    total_sum = total_sum + i
    total_count += 1 
    
    if i % 2 == 0:
        even_sum = even_sum + i
        even_count += 1
    else :                       # Using else instead of CONTINUE Statement
        odd_sum = odd_sum + i
        odd_count += 1

"""