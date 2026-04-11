import math
total_bill = float(input("Enter the total bill: "))
no_of_people = int(input("Enter number of people: "))
tip_percentage = float(input("Enter tip percentage: "))

tip_amount = (total_bill * tip_percentage) / 100
total_amount = total_bill + tip_amount
each_pays = total_amount / no_of_people
rounded_each_pays = round(each_pays,2)
ceil_each_pays = math.ceil(each_pays)
floor_each_pays = math.floor(each_pays)

print("===== Bill Split =====")
print(f"Bill Amount : {total_bill}")
print(f"Tip Amount  : {tip_amount}")
print(f"Total + Tip : {total_amount}")
print(f"Each Pays   : {rounded_each_pays}")
print(f"Each Pays ↑ : {ceil_each_pays}")
print(f"Each Pays ↓ : {floor_each_pays}")
print("======================")
