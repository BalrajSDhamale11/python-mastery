user1_name = "Arjun"
user1_age = 22

user2_name = "Sara"
user2_age = 25

temp_name = ""    #temp variable for storing name
temp_age = 0      #temp variable for storing age

print("Before Swap")
print(f"User1 : {user1_name}, Age {user1_age}")
print(f"User2 : {user2_name}, Age {user2_age}\n")

#swap logic for name
"""
temp_name = user1_name
user1_name = user2_name
user2_name = temp_name
"""

#tuple unpacking(for Age)
user1_name, user2_name = user2_name, user1_name

#tuple unpacking(for Name)
user1_age, user2_age = user2_age, user1_age

#swap logic for age
"""
temp_age = user1_age
user1_age = user2_age
user2_age = temp_age

"""

print("After Swap")
print(f"User1 : {user1_name}, Age {user1_age}")
print(f"User2 : {user2_name}, Age {user2_age}")