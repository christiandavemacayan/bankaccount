class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number  # Public attribute
        self.account_holder = account_holder  # Public attribute
        self._balance = initial_balance        # Protected attribute
        self.__transaction_history = []        # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.__transaction_history.append(f"Deposited: {amount}")
            print(f"Deposited: {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.__transaction_history.append(f"Withdrew: {amount}")
            print(f"Withdrew: {amount}. New balance: {self._balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self._balance

    def get_transaction_history(self):
        return self.__transaction_history

# Example usage
if __name__ == "__main__":
    account = BankAccount("123456789", "John Doe", 1000)
    
    print(f"Account Holder: {account.account_holder}")
    print(f"Account Number: {account.account_number}")
    
    account.deposit(500)
    account.withdraw(200)
    
    print(f"Current Balance: {account.get_balance()}")
    print("Transaction History:")
    for transaction in account.get_transaction_history():
        print(transaction)