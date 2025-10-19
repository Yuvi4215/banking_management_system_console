# core/services/account_service.py
import random
import uuid
from core.utils.timestamp_utils import get_timestamp
from core.database.file_manager import FileManager
from core.models.customer_model import Customer


def generate_uuid(length=8):
    """Generate a random lowercase alphanumeric UUID of given length."""
    return str(uuid.uuid4())[:length]


class AccountService:
    def __init__(self):
        self.identifier_db = FileManager("banking_management_system/core/database/identifier_data.json")
        self.account_db = FileManager("banking_management_system/core/database/account.json")
        self.customer_db = FileManager("banking_management_system/core/database/customer.json")
        # self.customer_db = FileManager("core/database/customer.json")
        self.transaction_db = FileManager("banking_management_system/core/database/transaction.json")

    def create_account(
        self, username, password, full_name, email, phone, address, balance=0.0
    ):
        account_no = random.randint(1111111, 9999999)
        uuid_key = generate_uuid()

        # --- Customer object ---
        customer = Customer(username, password, account_no, balance)

        # --- Identifier for fast identificarion ---
        identifier_data = {
            "account_no": account_no,
        }

        # --- Account info ---
        account_info = {
            "username": username,
            "password": password,
            "role": "CUSTOMER",
            "account_no": account_no,
            "balance": balance,
        }

        # --- Customer profile ---
        customer_profile = {
            "username": username,
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "address": address,
            "account_no": account_no,
        }

        # --- Initial deposit transaction ---
        initial_transaction = {
            "type": "DEPOSIT",
            "amount": balance,
            "date": get_timestamp(),
            "remark": "Account Opening Amount"
        }

        # --- Add to JSON files using UUID key ---
        self.account_db.add_record({uuid_key: account_info})
        self.customer_db.add_record({uuid_key: customer_profile})
        self.transaction_db.add_record({uuid_key: [initial_transaction]})
        self.identifier_db.add_record({uuid_key: identifier_data})

        print(
            f"Account created successfully!\nUUID: {uuid_key}\nAccount No: {account_no}"
        )
        return uuid_key, account_no
    
    
    def getAllCustomers(self):
        return self.customer_db.read_all()
    
    def getIdentifiers(self):
        return self.identifier_db.read_all()
    
    def deleteCustomer(self, account_no):
        pass

    def isPresent(self, account_no):
        data_dict=self.identifier_db.read_all()
        for key,value in data_dict.items():
            if value["account_no"]==account_no:
                return key
        return None

        # data_dict=self.getIdentifiers()
        # acc_list=[details['account_no'] for details in data_dict.values()]
        # if account_no in acc_list:
        #     return True
        # return False




# --- Example usage ---
if __name__ == "__main__":
    acc_service = AccountService()
    # acc_service.create_account(
    #     username="Sunny",
    #     password="password",
    #     full_name="Sunny Varma",
    #     email="sunny@example.com",
    #     phone="+91-9988776655",
    #     address="5 Fc Road, Pune",
    #     balance=1000,
    # )
    acc_service.getAllCustomers()
    # print(acc_service.getAllCustomers())
