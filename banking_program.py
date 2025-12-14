

def show_balance(balance):
    print(f"Your Balance is ${balance:.2f}")


def deposit():
    deposit_amount = float(input("Enter the amount to deposit: "))
    if deposit_amount < 0:
        print("Invalid amount!")
        return 0
    else:
        return deposit_amount
        

def withdraw(balance):
    withdraw_amount = float(input("Enter the amount you want to withdraw: "))
    if withdraw_amount > balance:
        print("Insufficient Funds!")
        return 0
    elif withdraw_amount < 0:
        print("Invalid amount entered!")
        return 0
    else:
        return withdraw_amount
        

def main():

    balance = 0
    is_running = True

    while is_running:
        print("******************")
        print(" Banking Program ")
        print("******************")
        print("1.Show Balance")
        print("2.Deposit amount")
        print("3.Withdraw amount")
        print("4.Exit")

        choice = input("Enter your choice(1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("That is not a valid choice.")
    print("Thank you! Have a nice day.")
            
if __name__ == '__main__':
    main()


