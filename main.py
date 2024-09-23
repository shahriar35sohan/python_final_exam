from Users import Customer, Admin
from Bank import Bank

def main():
    bank = Bank("USA Federal Bank", 25000000)
    
    johnny = Customer("Johnny", "johnny@gmail.com", "UK", "savings")
    rohan = Customer("Rohan", "rohan@gmail.com", "Australia", "current")
    lee = Admin("Bruce Lee", "lee@gmail.com","Admin")
    johnny.create_account(bank)
    rohan.create_account(bank)
    lee.create_account(bank)

    while True:
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. View Balance")
        print("4. View Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Delete User Account")
        print("8. View All Users")
        print("9. View Total Bank Balance")
        print("10. View Total Bank Loan")
        print("11. Loan Feature")
        print("12. Exit")

        n = int(input("Enter an option: "))

        if n == 1:
            deposit = int(input("Enter deposit amount: "))
            johnny.deposit(deposit)
        elif n == 2:
            draw = int(input("Enter withdrawal amount: "))
            johnny.withdraw(draw)
        elif n == 3:
            johnny.view_balance()
        elif n == 4:
            johnny.view_transaction_history()
        elif n == 5:
            amount = int(input("Enter loan amount: "))
            johnny.take_loan(amount)
        elif n == 6:
            amount = int(input("Enter transfer amount: "))
            johnny.transfer(rohan, amount)
        elif n == 7:
            lee.delete_account(rohan.account_number)
        elif n == 8:
            lee.view_users()
        elif n == 9:
            lee.view_total_balance()
        elif n == 10:
            lee.view_total_loan()
        elif n == 11:
            ability = input("Enter decision (y/n): ")
            if ability == 'y':
                lee.change_loan_feature(True)
            else:
                lee.change_loan_feature(False)
        else:
            break

if __name__ == '__main__':
    main()
