print("WELCOME TO ATM")
balance = 40000
pin=6465
min_balance = 500
while True:
    entered_pin=int(input("Please enter your four digit pin"))
    if(entered_pin == pin):
        print("Pin verification Successful")
        break
    else:
        print("Your pin numbrer is wrong!Please try again")
while True:
    print("-----ATM MENU-------")
    print("1.Check balance ")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice=int(input("Enter your choice:"))
    if(choice==1):
        print("Your balance is",balance)
    elif(choice==2):
        amount=int(input("Enter the deposit amount"))   
        balance += amount
        print("Amount added successfully")
        print("New balance is",balance)
    elif(choice==3):
        amount=int(input("Enter the withdraw amount"))
        if(balance - amount<min_balance):
            print("Minimum balance requirement not met.")
        elif(amount<=balance):
            balance -= amount
            print("Amount withdrawn successfully")
            print("New balance is",balance)
        else:
            print("Insufficient balance")
    elif(choice==4): 
        print("Thankyou for Visiting Us")
        break
    else:
        print("Invalid choice!Please try again")