from core.database.file_manager import FileManager
from core.services.account_service import AccountService
from core.utils.console_utils import (
    print_header,
    print_content,
    clear_screen,
    get_input,
    get_password
)
from core.models.customer_model import Customer


class LoginManager:
    def __init__(self):
        self.employee_db = FileManager(
            "banking_management_system/core/database/employee.json"
        )
        self.customer_db = FileManager(
            "banking_management_system/core/database/customer.json"
        )
        self.identifier_db = FileManager(
            "banking_management_system/core/database/identifier_data.json"
        )
        self.account_db = FileManager(
            "banking_management_system/core/database/account.json"
        )

    def login(self, role):
        clear_screen()
        print_header(f"🔐 {role.capitalize()} Login")
        username = get_input("Enter username  ", True)

        if role == "customer":
            # 🧩 Find encrypted_id by username
            encrypted_id = None
            data_dict = self.identifier_db.read_all()

            for key, value in data_dict.items():
                if value.get("username") == username:
                    encrypted_id = key
                    break

            # 🧩 If username not found
            if encrypted_id is None:
                print_content("Username not found!", "ERROR")
                get_input("Press Enter",False,0.95)
                return None, None

            password = get_password("Enter password ", True)
            user = self.account_db.getCustomer(encrypted_id)

            # 🧩 If user found and password matches
            if user and user.get("password") == password:
                print_content("Login successful!", "SUCCESS")
                get_input("Press Enter", False, 0.95)
                return (
                    Customer(
                        user["username"], None, user["account_no"], user["balance"]
                    ),
                    encrypted_id,
                )
            else:
                print_content("Wrong password!", "ERROR")
                get_input("Press Enter",False,0.95)
                return None, None

        else:
            # 🧩 Employee login
            user = self.employee_db.getEmployee(username)
            if not user:
                print_content("Username not found.", "ERROR")
                get_input("Press Enter",False,0.95)
                return None, None

            password = get_password("Enter password ", True)
            if user.get("password") == password:
                print_content("Login successful!", "SUCCESS")
                get_input("Press Enter", False, 0.95)
                return user, user["username"]
            else:
                print_content("Wrong password.", "ERROR")
                get_input("Press Enter",False,0.95)
                return None, None
