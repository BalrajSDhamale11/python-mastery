# 🔺 Level 2 — Logic Challenge
# "The Input Cleaner"

email = input("Enter email: ")
username = input("Enter username: ")
cleaned_email = email.strip().lower()
cleaned_username = username.strip()
if '_' in username:         #has_underscore = username.count('_') > 0 
    has_underscore = True   #has_underscore = username.find('_') != -1
else:
    has_underscore = False
if cleaned_username.startswith("raj"):
    starts_with_raj = True
email_length = len(cleaned_email)

print(f"Cleaned Email    : {cleaned_email}")
print(f"Cleaned Username : {cleaned_username}")
print(f"Has underscore   : {has_underscore}")
print(f"Starts with raj  : {starts_with_raj}")
print(f"Email length     : {email_length}")