import os
from datetime import datetime

balance_file = "balance.txt"
transaction_file = "transactions.txt"


if not os.path.exists(balance_file):
    with open(balance_file, "w") as file:
        file.write("1000")

with open(balance_file, "r") as file:
    balance = float(file.read())


pin = 1212
user_pin = int(input("Enter your 4 digit pin: "))

if user_pin != pin:
    print("Incorrect PIN. Access denied.")
    exit()
else:
    print("PIN verified successfully.")

def save_transaction(t_type, amount, balance):
    with open(transaction_file, "a") as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{time} | {t_type} | Amount: {amount} | Balance: {balance}\n")

print("Welcome to Bank Of Maharastra")

print("""
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
""")

choice = int(input("Enter your choice: "))


if choice == 1:
   deposit = float(input("Enter deposit amount: "))
   if deposit > 0:
        balance += deposit

        with open(balance_file, "w") as file:
            file.write(str(balance))

        save_transaction("Deposit", deposit, balance)

        print("Deposit successful.")


elif choice == 2:
    withdraw = float(input("Enter withdrawal amount: "))
    if withdraw <= balance:
        balance -= withdraw

        with open(balance_file, "w") as file:
            file.write(str(balance))

        save_transaction("Withdraw", withdraw, balance)

        print("Withdrawal successful.")



elif choice == 3:
    print("Your current balance is:", balance)


elif choice == 4:
    print("Thank you for banking with us. Goodbye...!")

else:
    print("Invalid choice.")
