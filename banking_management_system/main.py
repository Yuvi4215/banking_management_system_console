from core.utils.console_utils import print_header,print_content,clear_screen,get_input,print_main
from core.authentication.login_manager import LoginManager
from core.roles.accountManagerRole import AccountManagerRole
from core.roles.cashierRoles import CashierRole
from core.roles.customerRoles import CustomerRole


def main_menu():
    clear_screen()
    print_main("🏦 Banking Management System ")
    print_content("1️⃣  Customer Login","content")
    print_content("2️⃣  Cashier Login","content")
    print_content("3️⃣  Account Manager Login","content")
    print_content("0️⃣  Exit","content")


def main():
    login_manager = LoginManager()
    flag, attempt = True, 0
    while flag:
        main_menu()
        choice=get_input("Select an option ")
        # choice = input("\nSelect an option: ").strip()
        if choice == "1":
            user,encrypted_id = login_manager.login("customer")
            if user:
                # print(user.get_role())
                CustomerRole(user,encrypted_id).start()
        elif choice == "2":
            user,cashier_id = login_manager.login("cashier")
            if user:
                CashierRole(user,cashier_id).start()
        elif choice == "3":
            user,manager_id = login_manager.login("manager")
            if user:
                AccountManagerRole(user,manager_id).start()
        elif choice == "0":
            print_content("Exit from main menu","LOGOUT",0.85)
            flag = False
        else:
            attempt += 1
            print_content("Invalid option. Try again.","ERROR")
            print_content(f"Attempt number : {attempt} failed","content")
            get_input("Press Enter",False,0.95)
        if attempt > 2:
            flag = False
    print_main("Program terminated....")


if __name__ == "__main__":
    main()

