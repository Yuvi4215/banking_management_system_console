# from core.utils.console_utils import printHeader
# from core.utils.console_utils import printHeader

# from core.utils import color_utils, emoji_utils, format_utils
# from core.services.transaction_service import TransactionService
# from core.services.account_service import AccountService


class CustomerRole:
    
    def __init__(self, customer):
        """
        customer: an instance of core.models.customer_model.Customer
        """
        self.customer = customer
        # self.transaction_service = TransactionService()
        # self.account_service = AccountService()

    def show_menu(self):
        # print(f"💰 Customer: {self.customer.get_username()} Dashboard")
        print("💰 Customer Dashboard")
        print("1️⃣  View Account Details")
        print("2️⃣  Transfer Money")
        print("3️⃣  View Transaction History")
        print("4️⃣  Logout")

    def start(self):
        """Main customer interaction loop"""
        flag,attempt=True,0
        while flag:
            self.show_menu()
            choice = input("\n👉 Enter choice: ").strip()
            if choice == "1":
                print("Choice- 1")
                self.view_profile()
                pass
            elif choice == "2":
                print("Choice- 2")
                self.transfer_money()
                pass
            elif choice == "3":
                print("Choice- 3")
                self.view_transaction_history()
                pass
            elif choice == "4":
                print("Logging out")
                flag = False
            else:
                attempt += 1
                print("❌ Invalid option. Try again.")
                print(f"Attempt number : {attempt} failed")
            if attempt > 2:
                flag = False




        # while True:
        #     self.show_menu()
        #     choice = input("\n👉 Enter choice: ").strip()

        #     if choice == "1":
        #         self.view_profile()
        #     elif choice == "2":
        #         self.transfer_money()
        #     elif choice == "3":
        #         self.view_transaction_history()
        #     elif choice == "4":
        #         # color_utils.print_info("👋 Logging out...")
        #         break
        #     else:
        #         pass
                # color_utils.print_error("❌ Invalid choice, try again.")

    # ----------------------------------------------------------
    # Customer Operations
    # ----------------------------------------------------------

    def view_profile(self):
        print("view_profile(self)")
        
        pass
        # color_utils.print_header("👤 Your Account Details")
        # details = self.account_service.get_account_details(self.customer)
        # format_utils.print_table(details)

    def transfer_money(self):
        print("transfer_money(self)")
        pass
        # color_utils.print_header("💸 Transfer Money")
        # target_user = input("Enter recipient username: ").strip()
        # amount = input("Enter amount: ").strip()

        # try:
        #     amount = float(amount)
        #     result = self.transaction_service.transfer(self.customer, target_user, amount)
        #     if result:
        #         color_utils.print_success(f"✅ Transfer successful to {target_user}")
        # except ValueError:
        #     color_utils.print_error("❌ Invalid amount entered.")
        # except Exception as e:
        #     color_utils.print_error(f"⚠️ {e}")

    def view_transaction_history(self):
        print("view_transaction_history(self)")
        pass
        # color_utils.print_header("🧾 Transaction History")
        # transactions = self.transaction_service.get_user_transactions(self.customer)
        # format_utils.print_table(transactions)


if __name__=="__main__":
    c_role=CustomerRole("customer")
    c_role.start()