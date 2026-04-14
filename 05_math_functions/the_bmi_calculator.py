#Importing Module/Library
import math

# Taking user input
name = input("Enter name: ").strip()
weight = float(input("Enter weight: "))
weight_unit = input("Is weight in kg or lb?: ").strip().lower()
height = float(input("Enter height: "))
height_unit = input("Is height in m or ft?: ").strip().lower()

# Convert weight
if weight_unit == "kg":
    converted_weight = weight
else:
    converted_weight = weight / 2.20462

# Convert height
if height_unit == "m":
    converted_height = height
else:
    converted_height = height / 3.28084

# Calculating BMI and other calculatons
actual_bmi = converted_weight / pow(converted_height,2) #alternative [height ** 2] or [math.pow(height, 2)] 
rounded_bmi = round(actual_bmi,2)
ceiling_bmi = math.ceil(rounded_bmi)
floor_bmi = math.floor(rounded_bmi)
absolute_diff = abs(actual_bmi - rounded_bmi)
print(f"actual_bmi = {actual_bmi}")
print(f"rounded_bmi = {rounded_bmi}")

# Output
print(f"\n===== BMI Report for {name} =====")
print(f"Weight : {converted_weight:.2f} kg")
print(f"Height : {converted_height:.2f} m")
print(f"BMI : {rounded_bmi}")
print(f"Ceiling BMI : {ceiling_bmi}")
print(f"Floor BMI : {floor_bmi}")
print(f"Absolute diff : {absolute_diff:.2f}")
print(f"===============================")