from abc import ABC, abstractmethod
import uuid

class Bank:
    def __init__(self, name, initial_amount):
        self.name = name
        self.balance = initial_amount
        self.loan = True
        self.bankrupt = False
        self.users = []
        self.admins = []
        self.loan_amount = 0

    def receive_loan(self, amount, user):
        if self.loan == True:
             if amount > self.balance:
                  print("Does not have sufficient loan amount.")
             elif amount <= 0:
                  print("Invalid loan amount.")
             else:
                  user.loan += 1
                  user.loan_amount += amount
                  user.balance += amount
                  self.balance -= amount
                  self.loan_amount += amount
                  print(f'Loan amount {amount} granted. New balance: {user.balance}')
                  user.transaction_history.append(f'LOAN: {amount} || BALANCE: {user.balance}')
            
        else:
             print("Loan service is not available now.")
        if self.balance <= 0:
                print(" This bank has no funds.")

class User(ABC):
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.accounts = []

    @abstractmethod
    def create_account(self, bank):
        pass
class Customer(User):
    def __init__(self, name, email, address, account_type):
        super().__init__(name, email, address)
        self.account_type = account_type
        self.account_number = str(uuid.uuid4())
        self.balance = 0
        self.loan = 0
        self.loan_amount = 0
        self.transaction_history = []

    def create_account(self, bank):
        self.bank = bank
        self.bank.users.append(self)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposit successful. New balance: {self.balance}')
            self.transaction_history.append(f'DEPOSIT: {amount} || BALANCE: {self.balance}')
            
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Withdrawal amount exceeded.")
        else:
            self.balance -= amount
            print(f'Withdrawal successful. New balance: {self.balance}')
            self.transaction_history.append(f'WITHDRAW: {amount} || BALANCE: {self.balance}')
            

    def view_balance(self):
        print(f'Current balance: {self.balance}')

    def view_transaction_history(self):
        print("---------------")
        for transaction_data in self.transaction_history:
            print(transaction_data)
        print("---------------")

    def take_loan(self, amount):
        if self.loan < 2:
            self.bank.receive_loan( amount, self)
        else:
            print("Loan limit exceeded.")

    def transfer(self, other, amount):
        if amount > self.balance:
            print("Insufficient funds for transfer.")
        elif other is None:
            print("Account does not exist.")
        elif self.bank.bankrupt:
            print("sorry,Bank fully rupted.")
        else:
            self.balance -= amount
            other.receive_transfer(amount)
            self.transaction_history.append(f'TRANSFERRED: {amount} || BALANCE: {self.balance}')
            print(f'Transfer successful. New balance: {self.balance}')

    def receive_transfer(self, amount):
        self.balance += amount
        self.transaction_history.append(f'RECEIVED: {amount} || BALANCE: {self.balance}')
     
class Admin(User):
    def __init__(self, name, email, account_type):
        super().__init__(name, email, account_type)

    def create_account(self, bank):
        self.bank = bank
        self.bank.admins.append(self)

    def delete_account(self, account_number):
        for user in self.bank.users:
            if user.account_number == account_number:
                self.bank.users.remove(user)
                print(f'Account {account_number} deleted.')

        print(f'Account {account_number} not found.')

    def view_users(self):
        print("---------------")
        for user in self.bank.users:
            print(f"Name: {user.name}, Email: {user.email}, Balance: {user.balance}, Account: {user.account_number}")
        print("----------------")

    def view_total_balance(self):
        print(f'Total bank balance: {self.bank.balance}')

    def view_total_loan(self):
        print(f'Total bank loan amount: {self.bank.loan_amount}')

    def change_loan_feature(self, ability):
        self.bank.loan = ability
        if ability== True:
            print("Enable")
        else:
            print("Disable")

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