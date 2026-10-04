import re

mobile = input("Enter mobile number: ")

pattern = r"^[6-9]\d{9}$"

if re.fullmatch(pattern, mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
