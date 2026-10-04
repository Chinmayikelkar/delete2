# Q6. Read and write binary image file

source = input("Enter source image file name: ")
destination = input("Enter destination image file name: ")

with open(source, "rb") as source_file:
    image_data = source_file.read()

with open(destination, "wb") as destination_file:
    destination_file.write(image_data)

print("Image file copied successfully.")
