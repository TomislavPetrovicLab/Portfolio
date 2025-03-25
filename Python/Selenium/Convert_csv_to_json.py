import csv  # Import the CSV module to read CSV files
import json  # Import the JSON module to write data to a JSON file

# Define the paths for the input CSV file and output JSON file
csv_file = "saucedemo_test_data_Sheet1.csv"  # Update with the actual filename for the CSV input
json_file = "saucedemo_test_data_Sheet1.json"  # Define the output JSON file name

# Initialize an empty list to hold the data to be converted to JSON format
data = []

# Open the CSV file for reading
with open(csv_file, mode="r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)  # Create a CSV reader object to read the file
    next(csv_reader)  # Skip the header row to avoid including it in the data

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Append the relevant data from each row to the data list as a dictionary
        data.append({"username": row[0], "password": row[1]})

# Open the JSON file for writing
with open(json_file, mode="w", encoding="utf-8") as file:
    # Write the data to the JSON file in a readable format with an indent of 4 spaces
    json.dump({"saucedemo_test_data_Sheet1": data}, file, indent=4)

# Print a success message indicating that the JSON file has been created
print(f"✅ JSON file '{json_file}' created successfully!")
