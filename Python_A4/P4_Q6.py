import re

password = input("Enter password: ")

patterns = {
    "uppercase": r"[A-Z]",
    "lowercase": r"[a-z]",
    "digit": r"\d",
    "special character": r"[^A-Za-z0-9]"
}

valid = True

if len(password) < 8:
    print("Password must contain at least 8 characters.")
    valid = False

for requirement, pattern in patterns.items():
    if not re.search(pattern, password):
        print("Password must contain at least one " + requirement + ".")
        valid = False

if valid:
    print("Valid password")
else:
    print("Invalid password")
