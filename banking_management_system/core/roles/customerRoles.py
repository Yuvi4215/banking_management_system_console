# from core.utils.console_utils import printHeader
# from core.utils.console_utils import printHeader

from core.utils.console_utils import (
    print_header,
    print_content,
    clear_screen,
    get_input,
)
from core.utils.table_utils import create_table
from core.services.transaction_service import TransactionService
from core.services.account_service import AccountService
from core.services.upi_service import display_qrcode


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
        clear_screen()
        print_header(f"💰 Customer: {self.customer.get_username()} Dashboard")
        print_content("1️⃣  View Account Details", "content")
        print_content("2️⃣  Transfer Money", "content")
        print_content("3️⃣  View Transaction History", "content")
        print_content("4️⃣  Recive money Through UPI", "content")
        print_content("0️⃣  Logout", "content")

    def start(self):
        """Main customer interaction loop"""
        flag, attempt = True, 0
        while flag:
            self.show_menu()
            choice = get_input("👉 Enter choice ")
            if choice == "1":
                clear_screen()
                self.view_profile(self.encrypted_id)
                get_input("Press Enter", False, 0.95)
            elif choice == "2":
                clear_screen()
                self.transfer_money()
                get_input("Press Enter", False, 0.95)
            elif choice == "3":
                clear_screen()
                self.view_transaction_history(self.encrypted_id)
                get_input("Press Enter", False, 0.95)
            elif choice == "4":
                clear_screen()
                self.recive_money_through_upi(self.encrypted_id)
                get_input("Press Enter", False, 0.95)
            elif choice == "0":
                print_content("Logging out","LOGOUT",0.90)
                flag = False
                get_input("Press Enter", False, 0.95)
            else:
                attempt += 1
                print_content("Invalid option. Try again.", "ERROR")
                print_content(f"Attempt number : {attempt} failed", "content")
                get_input("Press Enter", False, 0.95)
            if attempt > 2:
                flag = False

    # ----------------------------------------------------------
    # Customer Operations
    # ----------------------------------------------------------

    def view_profile(self, encrypted_id):
        print_header("👤 Your Account Details")
        headers = ["Username", "Password", "Role", "Account Number", "Balance"]
        row = self.transaction_service.get_current_status(encrypted_id)
        create_table(headers, row, "Customer Account detailes.", 70, 55)

    def transfer_money(self):
        print_header("💸 Transfer Money")
        account_no = get_input("Enter recipient Account number  ")
        if account_no.isdigit():
            target_encrypted_id = self.account_service.isPresent(int(account_no))
            if target_encrypted_id:
                amount = get_input("Enter amount ")
                try:
                    amount = float(amount)
                    result = self.transaction_service.transfer(
                        self.encrypted_id, target_encrypted_id, amount
                    )
                    if result:
                        print_content(f"Transfer successful to {account_no}", "SUCCESS")
                except ValueError:
                    print_content("Invalid amount entered.", "ERROR")
                except Exception as e:
                    print_content(f"{e}", "WARNING")
            else:
                print_content(f"There is no Account with : {account_no}", "ERROR")
        else:
            print_content("Please enter valid Account Number.", "WARNING")

    def view_transaction_history(self, encrypted_id):
        print_header("🧾 Transaction History")
        headers = ["Type", "Amount", "Date", "Remark"]
        transactions = self.transaction_service.view_transactions(encrypted_id)

        if not transactions:
            print("No transactions found for this user.")
            return

        create_table(headers, transactions, "All Transactions", 70, 50)
    
    def recive_money_through_upi(self,encrypted_id):
        print_header("💸 Recive Money Through UPI")
        amount = get_input("Enter Amount ")
        
        try:
            amount = float(amount)
            if amount>0:
                display_qrcode(amount)
                recive = get_input("Transaction Done? (y/n): ")
                if recive.lower() in ("y","yes"):
                    result = self.transaction_service.recive_upi_money(encrypted_id,amount)
                    if result:
                        print_content(result, "SUCCESS")
                else:
                    print_content("Transaction Failled.","ERROR")
            else:
                print_content(" Deposit amount must be greater than 0.","WARNING")
        except ValueError:
            print_content("Invalid amount entered.", "ERROR")
        except Exception as e:
            print_content(f"{e}", "WARNING")
            



if __name__ == "__main__":
    c_role = CustomerRole("customer")
    c_role.start()
