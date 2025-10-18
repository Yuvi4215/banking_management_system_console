# from core.utils import color_utils, emoji_utils, format_utils
from core.utils.table_utils import create_table
from core.services.account_service import AccountService


class AccountManagerRole:

    def __init__(self, manager):
        """
        manager: instance of core.models.account_manager_model.AccountManager
        """
        self.manager = manager
        self.accountService = AccountService()

    def show_menu(self):
        print("🧾 Account Manager Dashboard")
        print("1️⃣  Create New Customer Account")
        print("2️⃣  View All Customers")
        print("3️⃣  Delete Customer Account")
        print("4️⃣  Logout")

    def start(self):
        """Main account manager loop"""
        flag,attempt=True,0
        while flag:
            self.show_menu()
            choice = input("\n👉 Enter choice: ").strip()

            if choice == "1":
                print("Choice-1")
                self.create_account()
            elif choice == "2":
                print("Choice-2")
                self.view_customers()
            elif choice == "3":
                print("Choice-3")
                self.delete_account()
            elif choice == "4":
                print("Choice-4")
                print("👋 Logging out...")
                break
            else:
                attempt += 1
                print("❌ Invalid option. Try again.")
                print(f"Attempt number : {attempt} failed")
            if attempt > 2:
                flag = False

    # ----------------------------------------------------------
    # Manager Operations
    # ----------------------------------------------------------

    def create_account(self):
        print("create_account(self)")
        # create_account(username, password, full_name, email, phone, address, balance=0.0):
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()
        full_name=input("Enter Full Name: ").strip()
        email= input("Enter Email ID: ").strip()
        phone= input("Enter Phone Number: ").strip()
        address=input("Enter Address: ").strip()
        balance = input("Enter initial balance: ").strip()
        try:
            balance= float(balance)
            # accountService=AccountService()
            newAccount=self.accountService.create_account(username,password,full_name,email, phone,address,balance)
            print(f"✅ Account created for {username}")
            print(f"Account number :: {newAccount.account_no}")
        except ValueError:
            print("❌ Invalid balance entered.")
        except Exception as e:
            print(f"⚠️ {e}")      
        
        
        
        
        
        # color_utils.print_header("🧩 Create New Customer Account")
        # username = input("Enter username: ").strip()
        # password = input("Enter password: ").strip()
        # balance = input("Enter initial balance: ").strip()

        # try:
        #     balance = float(balance)
        #     self.account_service.create_customer(username, password, balance)
        #     color_utils.print_success(f"✅ Account created for {username}")
        # except ValueError:
        #     color_utils.print_error("❌ Invalid balance entered.")
        # except Exception as e:
        #     color_utils.print_error(f"⚠️ {e}")
        pass

    def view_customers(self):
        print("view_customers(self)")
        
        headers = ["ID", "Username", "Full Name", "Email", "Phone", "Address", "Account No"]
        
        customers = self.accountService.getAllCustomers()
        
        # Convert dictionary into list of rows in one line
        rows = [[customer_id, *details.values()] for customer_id, details in customers.items()]
        
        # Call your table creation function
        create_table(headers, rows, "List of all customers.", 70, 30)



    def delete_account(self):
        print("delete_account(self)")
        # color_utils.print_header("🗑️ Delete Customer Account")
        account_no = input("Enter Account Number: ").strip()
        confirm = input(f"Are you sure you want to delete '{account_no}'? (y/n): ").strip().lower()
        
            

        if confirm == "y":
            print(f"🗑️ Account '{account_no}' delete operation started.")
            if self.accountService.isPresent(account_no):
                self.accountService.deleteCustomer(account_no)
            else:
               print(f"❌ There is no account with this number : {account_no}.") 
        else:
            print("✅ Deletion canceled.")
        

if __name__=="__main__":
    am1=AccountManagerRole()
    am1.start()
