# Q8. Data Security in File Handling
# This is a simple demonstration of storing data in encoded form.
# For real applications, use a proper cryptographic library.

import base64

filename = "secure.txt"

data = input("Enter data to store securely: ")

# Encode data before storing
encoded_data = base64.b64encode(data.encode()).decode()

with open(filename, "w") as file:
    file.write(encoded_data)

print("Data stored in encoded form.")

# Read and decode data
with open(filename, "r") as file:
    stored_data = file.read()

decoded_data = base64.b64decode(stored_data).decode()

print("Decoded data:", decoded_data)
