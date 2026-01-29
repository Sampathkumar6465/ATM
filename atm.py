print("WELCOME TO ATM")

# ---------------- PASSWORD CREATION & STORE IN FILE ----------------
while True:
    password = input("Create your password: ")

    if len(password) < 8:
        print("Password must be at least 8 characters long")
        continue

    has_upper = False
    has_lower = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True

    if has_upper and has_lower:
        with open("password.txt", "w") as file:
            file.write(password)
        print("Password created and saved successfully ")
        break
    else:
        print("Password must contain at least one uppercase and one lowercase letter")

# ---------------- PASSWORD LOGIN (READ FROM FILE) ----------------
with open("password.txt", "r") as file:
    saved_password = file.read()

while True:
    login_password = input("Enter your password to login: ")

    if login_password == saved_password:
        print("Password verification successful ")
        break
    else:
        print("Wrong password! Please try again")

# ---------------- PIN VERIFICATION ----------------
balance = 40000
pin = 6465
min_balance = 500

while True:
    entered_pin = int(input("Please enter your four digit pin: "))
    if entered_pin == pin:
        print("Pin verification successful ")
        break
    else:
        print("Your pin number is wrong! Please try again")

# ---------------- ATM MENU ----------------
while True:
    print("\n----- ATM MENU -----")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = int(input("Enter the deposit amount: "))
        balance += amount
        print("Amount deposited successfully")
        print("New balance is:", balance)

    elif choice == 3:
        amount = int(input("Enter the withdraw amount: "))
        if balance - amount < min_balance:
            print("Minimum balance requirement not met.")
        elif amount <= balance:
            balance -= amount
            print("Amount withdrawn successfully")
            print("New balance is:", balance)
        else:
            print("Insufficient balance")

    elif choice == 4:
        print("Thank you for visiting us ")
        break

    else:
        print("Invalid choice! Please try again")
