import csv
import json

# Read CSV and convert to JSON
csv_file = "saucedemo_test_data_Sheet1.csv"  # Update with the actual filename
json_file = "saucedemo_test_data_Sheet1.json"

data = []

with open(csv_file, mode="r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        data.append({"username": row[0], "password": row[1]})

# Save as JSON
with open(json_file, mode="w", encoding="utf-8") as file:
    json.dump({"saucedemo_test_data_Sheet1": data}, file, indent=4)

print(f"✅ JSON file '{json_file}' created successfully!")
