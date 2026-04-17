# 📝 Your Problem — Level 1
# "The Age Gate"

age = int(input("Enter your age: "))
#top-down from highest to lowest:
if age >= 60:                          ## highest first
    print("You are a Senoir Citizen.")
elif age >= 18:
    print("You are an Adult.")
elif age >= 13:
    print("You are a Teenager.")
else:                                  # catches everything remaining
    print("You are a Child.") 