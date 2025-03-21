# Python Weight Converter

# Function to get a valid weight input
while True:
    try:
        weight = float(input("Enter your weight: "))  # Try converting input to float
        if weight <= 0:
            print("Error: Weight must be a positive number.")
            continue
        break  # Exit loop if input is valid
    except ValueError:
        print("Error: Invalid number format. Please enter a valid weight.")

# Function to get a valid unit input
unit = input("Enter the unit (kg or lbs): ").strip().lower()
while unit not in ("kg", "lbs"):
    print(f"Error: '{unit}' is not valid. Please input 'kg' or 'lbs'.")
    unit = input("Enter the unit (kg or lbs): ").strip().lower()

# Convert weight based on the selected unit
if unit == "kg":
    converted_weight = weight * 2.20462  # Convert kg to lbs
    print(f"{weight} kg is {round(converted_weight, 1)} lbs.")
elif unit == "lbs":
    converted_weight = weight / 2.20462  # Convert lbs to kg
    print(f"{weight} lbs is {round(converted_weight, 1)} kg.")