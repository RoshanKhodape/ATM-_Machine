pin = 1212
user_pin = int(input("Enter your 4 digit pin: "))
if user_pin != pin:
    print("Incorrect PIN. Access denied.")
    exit()
else:
    print("PIN verified successfully.")


print("Welcome to Bank Of Maharastra")

print("""
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
""")
balance = 1000.0  

choice = int(input("Enter your choice: "))
if choice == 1:
    deposit=float(input("Enter amount to be deposited: "))
    if deposit > 0:
        print("Amount", deposit," deposited successfully.")
        print("New balance is:", balance + deposit)
    else:
        print("Invalid deposit amount.")
elif choice == 2:
    withdraw= float(input("Enter amount to be withdrawn: "))
    if withdraw > 0:
        if withdraw <= balance:
            print("Amount", withdraw , "withdrawn successfully.")
            print("New balance is:", balance - withdraw)
        else:
            print("Insufficient balance.")
elif choice == 3:
    
    print("Your current balance is:", balance)
elif choice == 4:
    print("Thank you for banking with us. Goodbye...!")

else:
    print("Invalid choice. Please select a valid option.")