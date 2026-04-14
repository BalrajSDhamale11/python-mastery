#To full fill each condition in the output this code was generated
set_username = "raj"
set_password = "pass123"

username = input("Enter username: ").strip().lower()
password = input("Enter password: ").strip()

if username == set_username and password == set_password:
    print("✅ Login Successful! Welcome, raj.")
elif username != set_username:
    print("❌ Username not found.")
elif password != set_password:              #for more clean code 
    print("⚠️ Wrong password. Try again.")  #remove this elif and use
else:                                       # else:
    print("❌ Username not found.")         #     print("⚠️ Wrong password. Try again.")

 # because   # If the code reaches here, the username was correct, so it must be the password