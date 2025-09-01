#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        """
        Function Description:
            Initializes a new checkbook with a balance of $0.00.

        Parameters:
            None

        Return:
            None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
            Adds the specified amount to the current balance.

        Parameters:
            amount (float): The amount to deposit.

        Return:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function Description:
            Deducts the specified amount from the balance if sufficient funds are available.

        Parameters:
            amount (float): The amount to withdraw.

        Return:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function Description:
            Displays the current account balance.

        Parameters:
            None

        Return:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Function Description:
        Runs a simple command-line interface for interacting with the Checkbook.
        Supports deposit, withdrawal, balance check, and exiting the program.

    Parameters:
        None

    Return:
        None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()