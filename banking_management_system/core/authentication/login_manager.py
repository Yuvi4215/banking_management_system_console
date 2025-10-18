# from core.authentication.encryption_manager import EncryptionManager
from core.database.file_manager import FileManager
from core.services.account_service import AccountService 
from core.utils.console_utils import clear_screen
from core.models.cashier_model import Customer

class LoginManager:
    def __init__(self):
        self.employee_db = FileManager("banking_management_system/core/database/employee.json")
        self.customer_db = FileManager("banking_management_system/core/database/customer.json")
        self.identifier_db = FileManager("banking_management_system/core/database/identifier_data.json")
        self.account_db = FileManager("banking_management_system/core/database/account.json")


    def login(self, role):
        # clear_screen()
        print(f"🔐 {role.capitalize()} Login")
        username = input("Enter username: ").strip()

        if role=="customer":
            encrypted_id=None
            data_dict=self.identifier_db.read_all()
            for key,value in data_dict.items():
                if value["username"]==username:
                    encrypted_id=key
                    print(key)
                    break
            password = input("Enter password: ")
            user =self.account_db.getCustomer(encrypted_id)
            if user["password"]==password:
                return Customer(user["username"], user["password"],user["account_no"],user["balance"])
            
            else:
                print("❌ No user Found!")
        else:
            user = self.employee_db.getEmployee(username)
            if user:
                print(user["password"])
                password = input("Enter password: ")
                
                if user["username"] == username and user["password"] == password:
                    print("✅ Login successful!\n")
                    return user
                else:
                    print("❌ wrong password.")




                # if user["username"] == username and user["password"] == self.encrypt.encrypt(password):
                #     print("✅ Login successful!\n")
                #     return user
                # else:
                #     print("❌ wrong password.")

            else:
                print("❌ Username not found.")
            return None

