import json
import os
from core.models.customer_model import Customer
from core.utils.timestamp_utils import get_timestamp


class TransactionService:
    ACCOUNT_FILE = "banking_management_system/core/database/account.json"
    TRANSACTION_FILE = "banking_management_system/core/database/transaction.json"

    def _find_user_id_by_account(self, account_no):
        """Helper: find the encrypted user ID using account number."""
        accounts = self._load_data(self.ACCOUNT_FILE)
        for user_id, details in accounts.items():
            if details["account_no"] == account_no:
                return user_id
        return None

    def get_current_status(self, encrypted_id):
        accounts = self._load_data(self.ACCOUNT_FILE)
        account = accounts.get(encrypted_id)
        if not account:
            return []

        # Return a list of values (for your table)
        return [list(account.values())]

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
        """Return list of transactions for a given user or all users."""
        data_dict = self._load_data(self.TRANSACTION_FILE)

        # 🧩 Filter transactions by user if encrypted_id is given
        if encrypted_id:
            transactions = data_dict.get(encrypted_id, [])
        else:
            # Combine all transactions from all users
            transactions = [txn for txns in data_dict.values() for txn in txns]

        if not transactions:
            return []

        # 🧩 Build a proper 2D list for the table
        rows = []
        for txn in transactions:
            # Ensure txn is a dict
            if isinstance(txn, dict):
                rows.append(
                    [
                        txn.get("type", "N/A"),
                        f"₹{txn.get('amount', '0')}",
                        txn.get("date", "Unknown"),
                        txn.get("remark", "No remark"),
                    ]
                )
        return rows

    def get_all_transactions(self, encrypted_id=None):
        """View all or specific account transactions."""
        # 🧾 Build structured data for table
        headers = ["Encrypted ID", "Type", "Amount", "Date", "Remark"]
        
        
        data_dict = self._load_data(self.TRANSACTION_FILE)

        # 🧩 If specific account requested
        if encrypted_id:
            if encrypted_id not in data_dict:
                return headers,[]
            # Transactions for a specific account
            transactions = {encrypted_id: data_dict[encrypted_id]}
        else:
            # 🧩 Combine all transactions across accounts
            transactions = data_dict

        # 🧩 If still empty
        if not transactions:
            return headers,[]

        rows = []

        for enc_id, txns in transactions.items():
            for txn in txns:
                rows.append(
                    [
                        enc_id,
                        txn.get("type", "N/A"),
                        txn.get("amount", "0"),
                        txn.get("date", "Unknown"),
                        txn.get("remark", "No remark"),
                    ]
                )

        # Return headers and rows (so UI/controller can display them)
        return headers, rows

    def deposit_by_account(self, cashier_id, account_no, amount):
        """Deposit money into a customer's account using account number."""
        accounts = self._load_data(self.ACCOUNT_FILE)
        transactions = self._load_data(self.TRANSACTION_FILE)

        # Find customer ID (encrypted_id) by account number
        customer_id = None
        for enc_id, data in accounts.items():
            if data["account_no"] == account_no:
                customer_id = enc_id
                break

        if not customer_id:
            return f"❌ Account number {account_no} not found."

        customer = self._load_customer(customer_id)

        try:
            amount = float(amount)
        except ValueError:
            return "❌ Invalid amount entered."

        if amount <= 0:
            return "⚠️ Deposit amount must be greater than 0."

        # --- Perform deposit ---
        customer.deposit(amount)
        self._save_customer(customer_id, customer)

        # --- Record transaction ---
        txn = {
            "type": "DEPOSIT",
            "amount": amount,
            "date": get_timestamp(),
            "remark": f"Deposited by cashier: {cashier_id}",
        }
        transactions.setdefault(customer_id, []).append(txn)
        self._save_data(self.TRANSACTION_FILE, transactions)

        return (
            f"✅ ₹{amount:.2f} deposited successfully into A/C {account_no}.\n"
            f"New balance: ₹{customer.get_balance():.2f}"
        )

    # -----------------------------------------------------------------

    def withdraw_by_account(self, cashier_id, account_no, amount):
        """Withdraw money from a customer's account using account number."""
        accounts = self._load_data(self.ACCOUNT_FILE)
        transactions = self._load_data(self.TRANSACTION_FILE)

        # Find customer ID (encrypted_id) by account number
        customer_id = None
        for enc_id, data in accounts.items():
            if data["account_no"] == account_no:
                customer_id = enc_id
                break

        if not customer_id:
            return f"❌ Account number {account_no} not found."

        customer = self._load_customer(customer_id)

        try:
            amount = float(amount)
        except ValueError:
            return "❌ Invalid amount entered."

        if amount <= 0:
            return "⚠️ Withdrawal amount must be greater than 0."

        # --- Perform withdrawal ---
        if not customer.withdraw(amount):
            return f"❌ Insufficient balance. Current balance: ₹{customer.get_balance():.2f}"

        self._save_customer(customer_id, customer)

        # --- Record transaction ---
        txn = {
            "type": "WITHDRAWAL",
            "amount": amount,
            "date": get_timestamp(),
            "remark": f"Withdrawn by cashier: {cashier_id}",
        }
        transactions.setdefault(customer_id, []).append(txn)
        self._save_data(self.TRANSACTION_FILE, transactions)

        return (
            f"✅ ₹{amount:.2f} withdrawn successfully from A/C {account_no}.\n"
            f"Remaining balance: ₹{customer.get_balance():.2f}"
        )
    

    def recive_upi_money(self, encrypted_id, amount):
        """Recive money into a customer's account using QR code."""
        transactions = self._load_data(self.TRANSACTION_FILE)

        customer = self._load_customer(encrypted_id)

        # --- Perform deposit ---
        customer.deposit(amount)
        self._save_customer(encrypted_id, customer)

        # --- Record transaction ---
        txn = {
            "type": "UPI-Recived",
            "amount": amount,
            "date": get_timestamp(),
            "remark": "Recived Through : UPI",
        }
        transactions.setdefault(encrypted_id, []).append(txn)
        self._save_data(self.TRANSACTION_FILE, transactions)

        return (
            f"₹{amount:.2f} Amount recived successfully."
            f"New balance: ₹{customer.get_balance():.2f}"
        )

