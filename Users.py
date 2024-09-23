from abc import ABC, abstractmethod
import uuid

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
         
