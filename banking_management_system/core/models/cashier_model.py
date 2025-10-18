from core.models.user import User
from core.models.customer_model import Customer

# from user import User
# from customer_model import Customer

class Cashier(User):
    """
    Represents a Cashier who handles customer transactions.
    """

    def __init__(self, username, password, branch="Main Branch"):
        super().__init__(username, password, "cashier")
        self.branch = branch

    def deposit_to_customer(self, customer, amount):
        """Deposit money into a customer's account."""
        if amount <= 0:
            print("❌ Invalid deposit amount.")
            return False
        customer.deposit(amount)
        print(f"✅ Deposited ₹{amount} to {customer.get_username()}.")
        return True

    def withdraw_from_customer(self, customer, amount):
        """Withdraw money from a customer's account."""
        if customer.withdraw(amount):
            print(f"✅ Withdrawn ₹{amount} from {customer.get_username()}.")
            return True
        print("⚠️ Insufficient funds.")
        return False

    def __str__(self):
        return f"Cashier: {self._username} ({self.branch})"
    
if __name__=="__main__":
    cs1=Customer("101","pass",1000)
    ca1=Cashier("cashier", "1234")
    ca1.deposit_to_customer(cs1,200)
    print(cs1)
    print(ca1)
