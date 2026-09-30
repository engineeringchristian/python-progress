temperature = input("Enter the temperature: ")

try:
    temperature = float(temperature)
except ValueError:
    print(f"{temperature} is an invalid numerical value")
    exit()

unit_in = input("Is this temperature in Celsius or Fahrenheit (C/F): ").upper()

if unit_in == "C":
    temperature = (9 * temperature) / 5 +32
    unit_out = "Fahrenheit"
elif unit_in == "F":
    temperature = (temperature - 32) * 5 / 9
    unit_out = "Celsius"
else:
    print(f"{unit_in} is an invalid unit of measurement")
    exit()

print(f"The temperature is {temperature:.1f} degrees {unit_out}")
