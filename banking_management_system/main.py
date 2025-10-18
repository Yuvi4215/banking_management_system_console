from core.utils.console_utils import clear_screen,get_input
from core.authentication.login_manager import LoginManager
from core.roles.accountManagerRole import AccountManagerRole
from core.roles.cashierRoles import CashierRole
from core.roles.customerRoles import CustomerRole


def main_menu():
    # clear_screen()
    print("=== 🏦 Banking Management System ===")
    print("1️⃣  Customer Login")
    print("2️⃣  Cashier Login")
    print("3️⃣  Account Manager Login")
    print("0️⃣  Exit")


def main():
    login_manager = LoginManager()
    flag, attempt = True, 0
    while flag:
        main_menu()
        choice = input("\nSelect an option: ").strip()
        if choice == "1":
            user = login_manager.login("customer")
            if user:
                CustomerRole(user).start()
        elif choice == "2":
            user = login_manager.login("cashier")
            if user:
                CashierRole(user).start()
        elif choice == "3":
            user = login_manager.login("manager")
            if user:
                AccountManagerRole(user).start()
        elif choice == "0":
            print("Logging out")
            flag = False
        else:
            attempt += 1
            print("❌ Invalid option. Try again.")
            print(f"Attempt number : {attempt} failed")
            get_input("Press Enter",False)
        if attempt > 2:
            flag = False
    print("Program terminated....")


if __name__ == "__main__":
    main()


# #####################################################################

# # test_utils.py (place at banking_management_system/)
# from core.utils.console_utils import print_header, print_content
# from core.utils.table_utils import create_table
# from core.utils.timestamp_utils import get_timestamp

# def main():
#     print_header("Utils Test")
#     print_content("All systems go", "SUCCESS")
#     headers = ["ID","Name","Balance"]
#     rows = [[1,"Alice","₹5000"], [2,"Bob","₹3000"]]
#     create_table(headers, rows, title="Accounts")
#     print("Timestamp:", get_timestamp())

# if __name__ == "__main__":
#     main()
