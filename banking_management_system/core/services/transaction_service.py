import json
import os
from core.models.customer_model import Customer
from core.utils.timestamp_utils import get_timestamp


class TransactionService:
    ACCOUNT_FILE = "banking_management_system/core/database/account.json"
    TRANSACTION_FILE = "banking_management_system/core/database/transaction.json"

    def _load_data(self, file_path):
        if not os.path.exists(file_path):
            return {}
        with open(file_path, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

    def _save_data(self, file_path, data):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

    def _load_customer(self, user_id):
        """Load a customer object from JSON using its ID."""
        accounts = self._load_data(self.ACCOUNT_FILE)
        if user_id not in accounts:
            return None
        data = accounts[user_id]
        return Customer(
            username=data["username"],
            password=data["password"],
            account_no=data["account_no"],
            balance=data["balance"],
        )

    def _save_customer(self, user_id, customer):
        """Save a customer's updated balance back to JSON."""
        accounts = self._load_data(self.ACCOUNT_FILE)
        accounts[user_id] = customer.to_dict()
        self._save_data(self.ACCOUNT_FILE, accounts)

    # -----------------------------------------------------------------

    def transfer(self, sender_id, receiver_id, amount):
        """Use Customer methods to transfer money between accounts."""
        transactions = self._load_data(self.TRANSACTION_FILE)

        sender = self._load_customer(sender_id)
        receiver = self._load_customer(receiver_id)

        if not sender or not receiver:
            return "❌ One or both accounts not found."

        try:
            amount = float(amount)
        except ValueError:
            return "❌ Invalid amount."

        if amount <= 0:
            return "⚠️ Amount must be greater than 0."

        # --- Use OOP methods here ---
        if not sender.withdraw(amount):
            return "❌ Insufficient balance!"

        receiver.deposit(amount)

        # --- Persist updated balances ---
        self._save_customer(sender_id, sender)
        self._save_customer(receiver_id, receiver)

        # --- Record transaction ---
        timestamp = get_timestamp()
        sender_txn = {
            "type": "TRANSFER SENT",
            "amount": amount,
            "date": timestamp,
            "remark": f"To {receiver.get_username()} ({receiver_id})",
        }
        receiver_txn = {
            "type": "TRANSFER RECEIVED",
            "amount": amount,
            "date": timestamp,
            "remark": f"From {sender.get_username()} ({sender_id})",
        }

        transactions.setdefault(sender_id, []).append(sender_txn)
        transactions.setdefault(receiver_id, []).append(receiver_txn)
        self._save_data(self.TRANSACTION_FILE, transactions)

        return (
            f"✅ Transfer successful!\n"
            f"{sender.get_username()} → {receiver.get_username()}\n"
            f"₹{amount} transferred.\n"
            f"Remaining balance: ₹{sender.get_balance():.2f}"
        )

    def view_transactions(self, encrypted_id=None):
        """View all or specific account transactions."""
        data_dict = self._load_data(self.TRANSACTION_FILE)

        # 🧩 If specific account requested
        if encrypted_id:
            if encrypted_id not in data_dict:
                return f"No transactions found for this User"

            transactions = data_dict[encrypted_id]
        else:
            # 🧩 Combine all transactions across accounts
            transactions = [txn for txns in data_dict.values() for txn in txns]

        # 🧩 If still empty
        if not transactions:
            return "No transactions found."

        # 🧾 Build formatted output
        result_lines = []
        for txn in transactions:
            result_lines.append(
                f"""\tType: {txn.get('type', 'N/A')}
        Amount: ₹{txn.get('amount', '0')}
        Date: {txn.get('date', 'Unknown')}
        Remark: {txn.get('remark', 'No remark')}
    """
            )

        # Join all transactions nicely
        result = "\n".join(result_lines)
        return result
