# from core.utils.console_utils import printHeader
# from core.utils.console_utils import printHeader

# from core.utils import color_utils, emoji_utils, format_utils
from core.services.transaction_service import TransactionService
from core.services.account_service import AccountService


class CustomerRole:

    def __init__(self, customer, encrypted_id):
        """
        customer: an instance of core.models.customer_model.Customer
        """
        self.customer = customer
        self.encrypted_id = encrypted_id
        self.transaction_service = TransactionService()
        self.account_service = AccountService()

    def show_menu(self):
        # print(f"💰 Customer: {self.customer.get_username()} Dashboard")
        print("💰 Customer Dashboard")
        print("1️⃣  View Account Details")
        print("2️⃣  Transfer Money")
        print("3️⃣  View Transaction History")
        print("4️⃣  Logout")

    def start(self):
        """Main customer interaction loop"""
        flag, attempt = True, 0
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
                print("Choice- 3", self.encrypted_id)
                self.view_transaction_history(self.encrypted_id)
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
        print(("👤 Your Account Details"))
        print(
            f"""
username       : {self.customer.get_username()}
Account Number : {self.customer.get_account_no()}
Balance        : {self.customer.get_balance()}

"""
        )

        pass
        # color_utils.print_header("👤 Your Account Details")
        # details = self.account_service.get_account_details(self.customer)
        # format_utils.print_table(details)

    def transfer_money(self):
        print("transfer_money(self)")
        print("💸 Transfer Money")
        account_no = input("Enter recipient Account number : ").strip()
        if account_no.isdigit():
            target_encrypted_id = self.account_service.isPresent(int(account_no))
            if target_encrypted_id:
                amount = input("Enter amount: ").strip()
                try:
                    amount = float(amount)
                    result = self.transaction_service.transfer(
                        self.encrypted_id, target_encrypted_id, amount
                    )
                    if result:
                        print(f"✅ Transfer successful to {account_no}")
                except ValueError:
                    print("❌ Invalid amount entered.")
                except Exception as e:
                    print(f"⚠️ {e}")
            else:
                print(f"There is no Account with : {account_no}")
        else:
            print("Please enter valid Account Number.")

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

    def view_transaction_history(self, encrypted_id):
        print("view_transaction_history(self)")
        print("🧾 Transaction History")
        # transactions = self.transaction_service._load_customer(encrypted_id)
        transactions= self.transaction_service.view_transactions(encrypted_id)
        print(transactions)

        pass
        # color_utils.print_header("🧾 Transaction History")
        # format_utils.print_table(transactions)


if __name__ == "__main__":
    c_role = CustomerRole("customer")
    c_role.start()
