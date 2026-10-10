pin = 1212
balance = 1000.0

user_pin = input("Enter your 4-digit PIN: ")

if user_pin != str(pin):
    print("Incorrect PIN. Access denied.")
else:
    print("PIN verified successfully.")
    print("Welcome to Bank of Maharashtra!")

    while True:
        print("""
        1. Deposit
        2. Withdraw
        3. Check Balance
        4. Exit
        """)

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                deposit = float(
                    input("Enter amount to deposit: ")
                )

                if deposit > 0:
                    balance += deposit
                    print("Deposit successful!")
                    print(f"New balance: ₹{balance:.2f}")
                else:
                    print("Invalid deposit amount.")

            elif choice == 2:
                withdraw = float(
                    input("Enter amount to withdraw: ")
                )

                if withdraw <= 0:
                    print("Invalid withdrawal amount.")
                elif withdraw <= balance:
                    balance -= withdraw
                    print("Withdrawal successful!")
                    print(f"New balance: ₹{balance:.2f}")
                else:
                    print("Insufficient balance.")

            elif choice == 3:
                print(f"Current balance: ₹{balance:.2f}")

            elif choice == 4:
                print("Thank you for banking with us!")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")
