# Q4. Read and write CSV file in tabular format

import csv

filename = "students.csv"

data = [
    ["Name", "City", "Marks(out of 100)"],
    ["Riya", "Pune", 80],
    ["Siya", "Nashik", 85],
    ["Krish", "Nagpur", 75]
]

# Write CSV file
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully.\n")

# Read CSV file
with open(filename, "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print("\t".join(row))
