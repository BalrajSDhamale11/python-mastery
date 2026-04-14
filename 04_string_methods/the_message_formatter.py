# 🔺 Level 3 — Full Integration
# "The Message Formatter"

message = input("Enter your message: ")
original = message
cleaned_m = message.strip()
uppercase_m = cleaned_m.upper()
split = cleaned_m.split()
word_count = len(split)
contains_raj = 'raj' in cleaned_m
startswith_hello = cleaned_m.startswith('hello')
endswith_raj = cleaned_m.endswith('raj!')
replace = cleaned_m.replace('raj', 'amit')

print("\n===== Message Report =====\n")

print(f"Original               : {original}")
print(f"Cleaned                : {cleaned_m}")
print(f"Uppercase              : {uppercase_m}")
print(f"Word Count             : {word_count}")
print(f"Contains 'raj'         : {contains_raj}")
print(f"Starts with 'hello'    : {startswith_hello}")
print(f"Ends with 'raj!'       : {endswith_raj}")
print(f"Replace 'raj' → 'amit' : {replace}")
print("\n==========================")