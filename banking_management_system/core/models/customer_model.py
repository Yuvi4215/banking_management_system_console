from user import User

# from core.models.user import User


class Customer(User):
    """
    Represents a bank customer.
    Inherits from User → Demonstrates Inheritance.
    """

    def __init__(self, username, password, balance=0.0):
        super().__init__(username, password, "customer")
        self.__balance = balance  # Private attribute

    # --- Encapsulation for balance ---
    def get_balance(self):
        return self.__balance

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
