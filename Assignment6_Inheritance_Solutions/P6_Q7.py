# Q7. Method Overriding - Payment Gateway

class PaymentGateway:
    def process_payment(self, amount):
        print(f"Processing payment of ₹{amount:.2f} through the payment gateway.")


class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Credit card payment of ₹{amount:.2f} processed.")


class UPIPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"UPI payment of ₹{amount:.2f} processed.")


def main():
    amount = float(input("Enter payment amount: ₹"))
    print("1. Credit card\n2. UPI")
    choice = input("Choose payment method: ")

    if choice == "1":
        payment = CreditCardPayment()
    elif choice == "2":
        payment = UPIPayment()
    else:
        print("Invalid payment method.")
        return

    payment.process_payment(amount)


if __name__ == "__main__":
    main()
