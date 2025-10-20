# from core.authentication.encryption_manager import EncryptionManager
from core.database.file_manager import FileManager
from core.services.account_service import AccountService 
from core.utils.console_utils import print_header,print_content,clear_screen,get_input
from core.models.cashier_model import Customer

class LoginManager:
    def __init__(self):
        self.employee_db = FileManager("banking_management_system/core/database/employee.json")
        self.customer_db = FileManager("banking_management_system/core/database/customer.json")
        self.identifier_db = FileManager("banking_management_system/core/database/identifier_data.json")
        self.account_db = FileManager("banking_management_system/core/database/account.json")


    def login(self, role):
        clear_screen()
        print_header(f"🔐 {role.capitalize()} Login")
        username = get_input("Enter username: ",True)

        if role=="customer":
            encrypted_id=None
            data_dict=self.identifier_db.read_all()
            for key,value in data_dict.items():
                if value["username"]==username:
                    encrypted_id=key
                    # print(key)
                    break
            password = get_input("Enter password: ",True)
            user =self.account_db.getCustomer(encrypted_id)
            if user["password"]==password:
                # print(Customer(user["username"], None ,user["account_no"],user["balance"]))
                return Customer(user["username"], None,user["account_no"],user["balance"]), encrypted_id
            
            else:
                print_content("No user Found!","ERROR")
        else:
            user = self.employee_db.getEmployee(username)
            if user:
                password = get_input("Enter password: ",True)
                
                if user["username"] == username and user["password"] == password:
                    print_content("Login successful!","SUCCESS")
                    get_input("Press Enter",False,0.95)
                    return user, user["username"]
                else:
                    print_content("wrong password.","ERROR")


            else:
                print_content("Username not found.","ERROR")
            return None
