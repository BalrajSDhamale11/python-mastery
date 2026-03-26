number = float(input("Enter a number: "))

to_int = int(number)
to_float = float(number) # or we can just keep the same
to_str = str(number)
to_bool = bool(number)


print(f"As int : {to_int}")
print(f"As float : {to_float}")
print(f'As str : \"{to_str}"')
print(f"As bool : {to_bool}")