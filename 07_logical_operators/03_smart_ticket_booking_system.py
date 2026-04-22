# 🔺 Level 3 — Full Integration
# "The Smart Ticket Booking System"

name = input("Enter name: ").strip()
age = int(input("Enter age: "))
is_tuesday = input("Is it Tuesday? (True/False): ").strip().lower() == "true"
is_member = input("Are you a Member? (True/False): ").strip().lower() == "true"
tuesday_discount = 0.0
member_discount = 0.0
# We determined Category and Base price 
if age >= 60:
    category = "Senior"
    base_price = 150
elif age >= 13:
    category = "Adult"
    base_price = 250
elif age >= 5:
    category = "Child"
    base_price = 100
else:
    category = "Infant"
    base_price = 0

# Applying Discounts
if base_price > 0:
    if is_tuesday:
        tuesday_discount = (base_price * 0.20)
    
    if is_member:
        member_discount = 50.0

final_price = base_price - tuesday_discount - member_discount

# 3. Display Result
print(f"\n===== 🎬 Ticket Summary for {name} =====")
print(f"Age          : {age}")
print(f"Category     : {category}")
print(f"Base Price   : ₹{base_price}")
print(f"Tuesday Disc : -₹{tuesday_discount:.2f}")
print(f"Member Disc  : -₹{member_discount:.2f}")
print(f"Final Price  : ₹{final_price:.2f}")
print("=====================================")