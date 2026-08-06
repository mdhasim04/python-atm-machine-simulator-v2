print("=" * 50)
print("         ATM MACHINE SIMULATOR")
print("=" * 50)

correct_pin = "1234"
balance = 10000
transaction_history = []

# PIN Verification (3 Attempts)
attempt = 0

while attempt < 3:
    pin = input("Enter 4-digit PIN: ")

    if pin == correct_pin:
        print("\nLogin Successful!\n")
        break
    else:
        attempt += 1
        print(f"Incorrect PIN! Attempts Left: {3 - attempt}")

if attempt == 3:
    print("\nATM Blocked! Too many incorrect attempts.")
    exit()

# ATM Menu
while True:

    print("\n========== ATM MENU ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Fast Cash")
    print("5. Transaction History")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"\nCurrent Balance: ₹{balance}")

    elif choice == "2":
        amount = float(input("Enter Deposit Amount: ₹"))

        if amount > 0:
            balance += amount
            transaction_history.append(f"Deposited ₹{amount}")
            print("Deposit Successful!")
        else:
            print("Invalid Amount!")

    elif choice == "3":
        amount = float(input("Enter Withdraw Amount: ₹"))

        if amount <= 0:
            print("Invalid Amount!")

        elif amount > balance:
            print("Insufficient Balance!")

        else:
            balance -= amount
            transaction_history.append(f"Withdraw ₹{amount}")
            print("Please collect your cash.")
            print(f"Remaining Balance: ₹{balance}")

    elif choice == "4":

        print("\nFast Cash")
        print("1. ₹500")
        print("2. ₹1000")
        print("3. ₹2000")

        fast = input("Choose Option: ")

        if fast == "1":
            amount = 500
        elif fast == "2":
            amount = 1000
        elif fast == "3":
            amount = 2000
        else:
            print("Invalid Option!")
            continue

        if amount <= balance:
            balance -= amount
            transaction_history.append(f"Fast Cash ₹{amount}")
            print(f"Please collect ₹{amount}")
        else:
            print("Insufficient Balance!")

    elif choice == "5":

        print("\n===== TRANSACTION HISTORY =====")

        if len(transaction_history) == 0:
            print("No Transactions Yet.")

        else:
            for transaction in transaction_history:
                print("-", transaction)

    elif choice == "6":
        print("\nThank You for Using Our ATM.")
        print(f"Final Balance: ₹{balance}")
        break

    else:
        print("Invalid Choice! Please try again.")