
print("Is the temperture in Celsius or Fahrenheit?")
unit = input("Enter C for Celsius or F for Fahrenheit: ").strip().upper()
temp = float(input("Enter the temperature value: "))

if unit == "C":
    converted_temp = round(temp * 9 / 5 + 32, 1)
    print(f"{temp} °C equals to: {converted_temp} °F")
elif unit == "F":
    converted_temp = round((temp - 32) * 5 / 9, 1)
    print(f"{temp} °F equals to: {converted_temp} °C")
else:
    print(f"Error: {unit} is not a valid unit of measurement")