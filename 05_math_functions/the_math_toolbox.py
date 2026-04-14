# 📝 Your Problem — Level 1
# "The Math Toolbox"

import math
#Input values
value_1 = float(input("Enter value 1: "))
value_2 = float(input("Enter value 2: "))
value_3 = float(input("Enter value 3: "))
# Math functions without importing math library
rounded_value = round(value_1)
absolute_value = abs(value_1)
raised_value = pow(value_2, 3)
max_value = max(value_1,value_2,value_3)
min_value = min(value_1,value_2,value_3)
# Math functions with importing math library
square_root = math.sqrt(value_3)
ceil_value = math.ceil(square_root)
floor_value = math.floor(square_root)
pi_value = math.pi

print("===== Math Toolbox =====\n ")
print("rounded_value  = " ,rounded_value)
print("absolute_value = " , absolute_value)
print("raised_value   = " , raised_value)
print("max_value      = " , max_value)
print("min_value      = " , min_value)
print("square_root    = " , square_root)
print("ceil_value     = " , ceil_value)
print("floor_value    = " , floor_value)
print("pi_value       = " , pi_value)
print("\n========================")
