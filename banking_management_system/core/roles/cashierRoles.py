# from core.utils import color_utils, emoji_utils, format_utils
from core.services.transaction_service import TransactionService
from core.services.account_service import AccountService


class CashierRole:
    
    def __init__(self, cashier,cashier_id):
        """
        cashier: instance of core.models.cashier_model.Cashier
        """
        self.cashier = cashier
        self.cashier_id=cashier_id
        self.transaction_service = TransactionService()
        self.account_service = AccountService()

    def show_menu(self):
        print("🏦 Cashier Dashboard")
        print("1️⃣  Deposit Money")
        print("2️⃣  Withdraw Money")
        print("3️⃣  View All Transactions")
        print("4️⃣  Logout")

    def start(self):
        """Main cashier loop"""

        flag,attempt=True,0
        while flag:
            self.show_menu()
            choice = input("\n👉 Enter choice: ").strip()

            if choice == "1":
                self.deposit_money()
            elif choice == "2":
                self.withdraw_money()
            elif choice == "3":
                self.view_all_transactions()
            elif choice == "4":
                print("👋 Logging out...")
                # color_utils.print_info("👋 Logging out...")
                break
            else:
                # color_utils.print_error("❌ Invalid choice, try again.")
                attempt += 1
                print("❌ Invalid option. Try again.")
                print(f"Attempt number : {attempt} failed")
            if attempt > 2:
                flag = False

    # ----------------------------------------------------------
    # Cashier Operations
    # ----------------------------------------------------------
    def deposit_money(self):
        print("💰 Deposit Money")
        try:
            account_no = int(input("Enter account number: ").strip())
            amount = float(input("Enter deposit amount: ").strip())
            result = self.transaction_service.deposit_by_account(self.cashier_id, account_no, amount)
            print(result)
        except Exception as e:
            print(f"⚠️ {e}")

    def withdraw_money(self):
        print("🏧 Withdraw Money")
        try:
            account_no = int(input("Enter account number: ").strip())
            amount = float(input("Enter withdrawal amount: ").strip())
            result = self.transaction_service.withdraw_by_account(self.cashier_id, account_no, amount)
            print(result)
        except Exception as e:
            print(f"⚠️ {e}")


    def view_all_transactions(self):
        print("view_all_transactions(self)")

        print("🧾 All Transactions")
        transactions = self.transaction_service.get_all_transactions()
        print(transactions)



        # color_utils.print_header("🧾 All Transactions")
        # transactions = self.transaction_service.get_all_transactions()
        # format_utils.print_table(transactions)
        pass



























    # def deposit_money(self):
    #     print("deposit_money(self)")
    #     # color_utils.print_header("💰 Deposit Money")
    #     # username = input("Enter customer username: ").strip()
    #     # amount = input("Enter amount to deposit: ").strip()

    #     # try:
    #     #     amount = float(amount)
    #     #     self.transaction_service.deposit(self.cashier, username, amount)
    #     #     color_utils.print_success(f"✅ Deposited ₹{amount:.2f} to {username}")
    #     # except Exception as e:
    #     #     color_utils.print_error(f"⚠️ {e}")
    #     pass

    # def withdraw_money(self):
    #     print("withdraw_money(self)")
    #     # color_utils.print_header("🏧 Withdraw Money")
    #     # username = input("Enter customer username: ").strip()
    #     # amount = input("Enter amount to withdraw: ").strip()

    #     # try:
    #     #     amount = float(amount)
    #     #     self.transaction_service.withdraw(self.cashier, username, amount)
    #     #     color_utils.print_success(f"✅ Withdrawn ₹{amount:.2f} from {username}")
    #     # except Exception as e:
    #     #     color_utils.print_error(f"⚠️ {e}")
    #     pass




if __name__ == "__main__":
    c_role = CashierRole()
    c_role.start()
