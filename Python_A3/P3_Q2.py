# Q2. Read specific file content
# a. Read first n lines
# b. Read last n lines
# c. Read specific n lines

filename = input("Enter file name: ")

with open(filename, "r") as file:
    lines = file.readlines()

print("\n1. Read first n lines")
print("2. Read last n lines")
print("3. Read specific n lines")

choice = int(input("Enter your choice: "))

if choice == 1:
    n = int(input("Enter number of lines: "))

    print("\nFirst", n, "lines:")
    for line in lines[:n]:
        print(line, end="")

elif choice == 2:
    n = int(input("Enter number of lines: "))

    print("\nLast", n, "lines:")
    for line in lines[-n:]:
        print(line, end="")

elif choice == 3:
    start = int(input("Enter starting line number: "))
    n = int(input("Enter number of lines: "))

    start_index = start - 1

    print("\nSelected lines:")
    for line in lines[start_index:start_index + n]:
        print(line, end="")

else:
    print("Invalid choice.")
