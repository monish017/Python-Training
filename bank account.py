class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance
    
    def __repr__(self):
        return f'account_number: "{self.account_number}", balance: {self.balance}'

# Example Test Case
account = BankAccount(account_number="12345678", initial_balance=1000)
print(account)  # Output: account_number: "12345678", balance: 1000
