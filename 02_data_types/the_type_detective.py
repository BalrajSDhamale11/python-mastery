# 🔺 Level 2 — Logic Challenge
# "The Type Detective"

a = 100
b = "100"
c = 100.0
d = False
e = "True"
f = 0

predicted_a = "int"
predicted_b = "string"
predicted_c = "float"
predicted_d = "boolean"
predicted_e = "string"
predicted_f = "int"

print(f"a -> I predicted: {predicted_a}     | Actual: {type(a)}")
print(f"b -> I predicted: {predicted_b}  | Actual: {type(b)}")
print(f"c -> I predicted: {predicted_c}   | Actual: {type(c)}")
print(f"d -> I predicted: {predicted_d} | Actual: {type(d)}")
print(f"e -> I predicted: {predicted_e}  | Actual: {type(e)}")
print(f"f -> I predicted: {predicted_f}     | Actual: {type(f)}")