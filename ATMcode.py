pin = 2026
balance = 12345

user_pin = int(input("Enter PIN: "))

if user_pin == pin:
    print("\nLogin Successful!\n")

    while True:
        print("-----OPTIONS-----")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. EXIT")
    
        option = int(input("Enter your option: "))

        match option:
            case 1:
                print("Current Balance",balance)
            case 2:
                amount = int(input("Enter amount to withdraw: "))
                if amount <= balance:
                    balance = balance - amount
                    print("Withdraw Successful!")
                    print("Remaining Balance",balance)
                else :
                    print("Insufficient Balance")
            case 3:
                amount = int(input("Enter amount to deposit: "))
                balance = balance + amount
                print("Deposit Successful!")
                print("Updated Balance",balance)
            case 4:
                print("Thank you for using ATM!")
            case _:
                print("Invalid option! Try again.")

else :
    print("Incorrect PIN!")