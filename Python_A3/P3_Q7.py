# Q7. Split large file into smaller 10-line files

filename = input("Enter large file name: ")

lines_per_file = 10

with open(filename, "r") as file:
    lines = file.readlines()

file_number = 1

for i in range(0, len(lines), lines_per_file):
    output_file = f"part_{file_number}.txt"

    with open(output_file, "w") as file:
        file.writelines(lines[i:i + lines_per_file])

    print(output_file, "created successfully.")
    file_number += 1

print("File splitting completed.")
