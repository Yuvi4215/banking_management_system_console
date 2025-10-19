# from user import User

from core.models.user import User


class Customer(User):
    """
    Represents a bank customer.
    Inherits from User → Demonstrates Inheritance.
    """

    def __init__(self, username, password,account_no, balance=0.0):
        super().__init__(username, password, "customer")
        self._account_no=account_no
        self.__balance = balance  # Private attribute

    # --- Encapsulation for balance ---
    def get_username(self):
        return super().get_username()
    
    def get_balance(self):
        return self.__balance
    
    def get_account_no(self):
        return self._account_no

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def to_dict(self):
        """Convert the customer object to a dictionary."""
        return {
            "username": self.get_username(),   
            "password": self._password,        
            "role": self.get_role(),           
            "account_no": self.get_account_no(),
            "balance": self.get_balance()
        }

    def __str__(self):
        return f"Customer: {self._username}, Balance: ₹{self.__balance}"


if __name__ == "__main__":
    c1 = Customer("101", "pass", 1000)
    print(c1)
    print(c1.get_balance())
    print(c1.withdraw(200))
    print(c1.get_balance())
    print(c1.deposit(69))
    print(c1.get_balance())
