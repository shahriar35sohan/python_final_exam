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

            
