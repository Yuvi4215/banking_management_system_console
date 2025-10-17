# from core.utils import color_utils, emoji_utils, format_utils
# from core.services.account_service import AccountService


class AccountManagerRole:
    def __init__(self):
    # def __init__(self, manager):
        """
        manager: instance of core.models.account_manager_model.AccountManager
        """
        # self.manager = manager
        # self.account_service = AccountService()

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
        # color_utils.print_header("📋 Customer List")
        # customers = self.account_service.get_all_customers()
        # format_utils.print_table(customers)
        pass

    def delete_account(self):
        print("delete_account(self)")
        # color_utils.print_header("🗑️ Delete Customer Account")
        # username = input("Enter username to delete: ").strip()
        # confirm = input(f"Are you sure you want to delete '{username}'? (y/n): ").strip().lower()

        # if confirm == "y":
        #     self.account_service.delete_customer(username)
        #     color_utils.print_success(f"🗑️ Account '{username}' deleted.")
        # else:
        #     color_utils.print_info("✅ Deletion canceled.")
        pass

if __name__=="__main__":
    am1=AccountManagerRole()
    am1.start()
