from core.utils.console_utils import print_header,print_content,clear_screen,get_input
from core.utils.table_utils import create_table
from core.services.account_service import AccountService


class AccountManagerRole:

    def __init__(self, manager, manager_id):
        """
        manager: instance of core.models.account_manager_model.AccountManager
        """
        self.manager = manager
        self.manager_id = manager_id
        self.accountService = AccountService()

    def show_menu(self):
        clear_screen()
        print_header(f"🧾 Profile: {self.manager["username"]} Dashboard")
        print_content("1️⃣  Create New Customer Account","content")
        print_content("2️⃣  View All Customers","content")
        print_content("3️⃣  Delete Customer Account","content")
        print_content("4️⃣  Logout","content")

    def start(self):
        """Main account manager loop"""
        flag, attempt = True, 0
        while flag:
            self.show_menu()
            choice = get_input("👉 Enter choice ")

            if choice == "1":
                clear_screen()
                self.create_account()
                get_input("Press Enter",False,0.95)
            elif choice == "2":
                clear_screen()
                self.view_customers()
                get_input("Press Enter",False,0.95)
            elif choice == "3":
                clear_screen()
                self.delete_account()
                get_input("Press Enter",False,0.95)
            elif choice == "4":
                # clear_screen()
                print_content("Logging out","LOGOUT",0.90)
                get_input("Press Enter",False,0.95)
                flag = False
            else:
                attempt += 1
                print_content("Invalid option. Try again.","ERROR")
                print_content(f"Attempt number : {attempt} failed","content")
                get_input("Press Enter",False,0.95)
            if attempt > 2:
                flag = False

    # ----------------------------------------------------------
    # Manager Operations
    # ----------------------------------------------------------


    def create_account(self):
        print_header("Account Creation Form")
        print_content("Set of rules for each fields", "INFO")
        print_content("1. Username and password filed first 5 characters are considered", "content")
        print_content("2. Full Name contain only String and length limit is 15", "content")
        print_content("3. Email Should end with @gmail.com and length limit is 15", "content")
        print_content("4. Phone number should only containt digits and lenght limit is 10", "content")
        print_content("5. Balance should be positive number", "content")


        # --- Username check ---
        while True:
            username = get_input("Enter Username ").lower()[:5]
            if self.accountService.is_username_available(username):
                break
            print_content(f"Username '{username}' is already taken. Try another one.", "WARNING")

        # --- Password ---
        password = get_input("Enter Password ")[:5]

        # --- Full name validation (no numbers allowed) ---
        while True:
            full_name = get_input("Enter Full Name ")[:15]
            if not any(char.isdigit() for char in full_name):
                break
            print_content("Full Name should not contain numbers. Try again.", "WARNING")

        # --- Email validation (must end with @gmail.com) ---
        while True:
            email = get_input("Enter Email ID ")[:15]  # Allow longer emails
            if email.endswith("@gmail.com"):
                break
            print_content("Email must end with '@gmail.com'. Try again.", "WARNING")

        # --- Phone validation (numbers only) ---
        while True:
            phone = get_input("Enter Phone Number ")[:10]
            if phone.isdigit():
                break
            print_content("Phone number must contain only digits. Try again.", "WARNING")

        # --- Address ---
        address = get_input("Enter Address ")[:50]

        # --- Initial balance ---
        while True:
            balance = get_input("Enter initial balance ")
            try:
                balance = float(balance)
                if balance < 0:
                    raise ValueError
                break
            except ValueError:
                print_content("Invalid balance entered. Enter a positive number.", "WARNING")

        try:
            newAccount, account_no = self.accountService.create_account(
                username, password, full_name, email, phone, address, balance
            )
            print_content(f"Account created for {username}", "SUCCESS")
            print_content(f"Account number :: {account_no}", "USER")
        except Exception as e:
            print_content(f"Exception: {e}", "WARNING")

    def view_customers(self):
        print_header("All Customers Detailes")

        headers = [
            "ID",
            "Username",
            "Full Name",
            "Email",
            "Phone",
            "Address",
            "Account No",
        ]

        customers = self.accountService.getAllCustomers()

        # Convert dictionary into list of rows in one line
        rows = [
            [customer_id, *details.values()]
            for customer_id, details in customers.items()
        ]

        # Call your table creation function
        create_table(headers, rows, "List of all customers.", 70, 30)

    def delete_account(self):
        print_header("Account Delete Operation.")
        # color_utils.print_header("🗑️ Delete Customer Account")
        account_no = get_input("Enter Account Number ")
        confirm = (
            get_input(f"Are you sure you want to delete '{account_no}'? (y/n): ")
            .lower()
        )

        if account_no.isdigit():
            if confirm == "y":
                account_no=int(account_no)
                print_content(f"🗑️  Account '{account_no}' delete operation started.","content")
                encrypted_id = self.accountService.isPresent(account_no)
                # print(encrypted_id)
                if encrypted_id:
                    if self.accountService.deleteCustomer(encrypted_id):
                        print_content(f"Account '{account_no}' deleted 🗑️","SUCCESS")
                else:
                    print_content(f"There is no account with this number : {account_no}.","ERROR")
            else:
                print_content("Deletion canceled.","WARNING")
        else:
            print_content("Account number should only be digits.","WARNING")

if __name__ == "__main__":
    am1 = AccountManagerRole()
    am1.start()
