# Q3. Using switch case perform the following
# a. Rename multiple files with prefix
# b. Copy file using binary mode
# c. List all files in directory and save
#
# Python 3.10+ is required for match-case.

import os
import shutil

print("1. Rename multiple files with prefix")
print("2. Copy file using binary mode")
print("3. List all files in directory and save")

choice = int(input("Enter your choice: "))

match choice:

    case 1:
        directory = input("Enter directory path: ")
        prefix = input("Enter prefix: ")

        count = 0

        for filename in os.listdir(directory):
            old_path = os.path.join(directory, filename)

            if os.path.isfile(old_path):
                new_name = prefix + filename
                new_path = os.path.join(directory, new_name)

                os.rename(old_path, new_path)
                count += 1

        print(count, "file(s) renamed successfully.")

    case 2:
        source = input("Enter source file name: ")
        destination = input("Enter destination file name: ")

        with open(source, "rb") as source_file:
            with open(destination, "wb") as destination_file:
                destination_file.write(source_file.read())

        print("File copied successfully using binary mode.")

    case 3:
        directory = input("Enter directory path: ")
        output_file = input("Enter output file name: ")

        files = os.listdir(directory)

        with open(output_file, "w") as file:
            for filename in files:
                file.write(filename + "\n")

        print("File list saved successfully.")

    case _:
        print("Invalid choice.")
