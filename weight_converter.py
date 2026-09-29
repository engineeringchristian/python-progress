weight = float(input("Enter your weight: "))
unit_in = input("Kilograms or pounds? (K or L):").upper()

if unit_in == "K":
    weight = weight * 2.205
    unit_out = "pounds"
elif unit_in == "L":
    weight = weight / 2.205
    unit_out = "kilograms"
else:
    print("Invalid input")
    exit()

print(f"Your weight is {weight:.2f} {unit_out}")
