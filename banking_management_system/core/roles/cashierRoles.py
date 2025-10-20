from core.utils.console_utils  import print_header,print_content,clear_screen,get_input
from core.utils.table_utils import create_table
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
        clear_screen()
        print_header("🏦 Cashier Dashboard")
        print_content("1️⃣  Deposit Money","content")
        print_content("2️⃣  Withdraw Money","content")
        print_content("3️⃣  View All Transactions","content")
        print_content("4️⃣  Logout","content")

    def start(self):
        """Main cashier loop"""

        flag,attempt=True,0
        while flag:
            self.show_menu()
            choice = get_input("👉 Enter choice: ")

            if choice == "1":
                clear_screen()
                self.deposit_money()
                get_input("Press Enter",False,0.95)
            elif choice == "2":
                clear_screen()
                self.withdraw_money()
                get_input("Press Enter",False,0.95)
            elif choice == "3":
                clear_screen()
                self.view_all_transactions()
                get_input("Press Enter",False,0.95)
            elif choice == "4":
                clear_screen()
                print_content("👋 Logging out...","LOGOUT",0.90)
                get_input("Press Enter",False,0.95)
                # color_utils.print_info("👋 Logging out...")
                flag = False
            else:
                attempt += 1
                print_content("❌ Invalid option. Try again.","ERROR")
                print_content(f"Attempt number : {attempt} failed","content")
                get_input("Press Enter",False,0.95)
            if attempt > 2:
                flag = False

    # ----------------------------------------------------------
    # Cashier Operations
    # ----------------------------------------------------------
    def deposit_money(self):
        print_header("💰 Deposit Money")
        try:
            account_no = int(get_input("Enter account number "))
            amount = float(get_input("Enter deposit amount "))
            result = self.transaction_service.deposit_by_account(self.cashier_id, account_no, amount)
            print_content(result,"SUCCESS")
        except Exception as e:
            print_content(f"{e}","WARNING")

    def withdraw_money(self):
        print_header("🏧 Withdraw Money")
        try:
            account_no = int(get_input("Enter account number "))
            amount = float(get_input("Enter withdrawal amount "))
            result = self.transaction_service.withdraw_by_account(self.cashier_id, account_no, amount)
            print_content(result,"SUCCESS")
        except Exception as e:
            print_content(f"{e}","WARNING")


    def view_all_transactions(self):
        print_header("🧾 All Transactions")
        headers, transactions = self.transaction_service.get_all_transactions()
        create_table(headers, transactions, "List of all transactions.", 70, 40)

if __name__ == "__main__":
    c_role = CashierRole()
    c_role.start()
