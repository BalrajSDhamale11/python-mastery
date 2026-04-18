# 📝 Your Problem — Level 1
# "The Amusement Park Entry"

age = int(input("Enter age: "))
height = float(input("Enter height (cm): "))
has_permission = (input("Has parent permission? (True/False): ")).strip() == "True"

is_tall_enough = height >= 140
is_old_enough = age >= 12
is_adult = age >= 18

if is_tall_enough and is_old_enough and (is_adult or has_permission):
    print("✅ Entry Allowed!")
elif not is_old_enough and not is_tall_enough:   # ← check BOTH first
    print("❌ Too young and too short.")
elif not is_old_enough:
    print("❌ Too young for this ride.")
elif not is_tall_enough:
    print("❌ Too short for this ride.")
elif not is_adult and not has_permission:
    print("❌ Need parent permission.")

# Option 1 (Simplified way): 
# elif not (is_adult or has_permission):
#    print("❌ Need parent permission.")

# Option 2 (Even Cleaner using De Morgan's Law)
# elif not is_adult and not has_permission:
#    print("❌ Need parent permission.")