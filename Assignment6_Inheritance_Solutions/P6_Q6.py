# Q6. Hybrid Inheritance - Device Application
# The PDF does not specify the remaining derived class or its method.
# This example demonstrates hybrid inheritance using a hierarchical branch
# (Laptop and Smartphone) combined with another inheritance level (GamingLaptop).

class Device:
    def device_details(self, device_id, powered):
        self.device_id = device_id
        self.powered = powered

    def display_device_details(self):
        print(f"Device ID: {self.device_id}")
        print(f"Powered on: {self.powered}")


class Laptop(Device):
    def device_details(self, device_id, powered, brand):
        super().device_details(device_id, powered)
        self.brand = brand

    def display_details(self):
        self.display_device_details()
        print(f"Laptop brand: {self.brand}")


class Smartphone(Device):
    def device_details(self, device_id, powered, brand):
        super().device_details(device_id, powered)
        self.brand = brand

    def display_details(self):
        self.display_device_details()
        print(f"Smartphone brand: {self.brand}")


class GamingLaptop(Laptop):
    def gaming_details(self, graphics_card):
        self.graphics_card = graphics_card

    def display_details(self):
        super().display_details()
        print(f"Graphics card: {self.graphics_card}")


def main():
    print("1. Laptop\n2. Smartphone\n3. Gaming laptop")
    choice = input("Choose device type: ")
    device_id = input("Enter device ID: ")
    powered_text = input("Is it powered on? (yes/no): ").strip().lower()
    powered = powered_text in ("yes", "y", "true", "1")
    brand = input("Enter brand: ")

    if choice == "1":
        device = Laptop()
        device.device_details(device_id, powered, brand)
    elif choice == "2":
        device = Smartphone()
        device.device_details(device_id, powered, brand)
    elif choice == "3":
        device = GamingLaptop()
        device.device_details(device_id, powered, brand)
        device.gaming_details(input("Enter graphics card: "))
    else:
        print("Invalid device type.")
        return

    print("\n--- Device Details ---")
    device.display_details()


if __name__ == "__main__":
    main()
