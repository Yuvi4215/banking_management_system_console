from core.utils.console_utils import print_header,print_content,clear_screen,get_input,print_main
from core.authentication.login_manager import LoginManager
from core.roles.accountManagerRole import AccountManagerRole
from core.roles.cashierRoles import CashierRole
from core.roles.customerRoles import CustomerRole
from assets.banner import banner
from assets.instruction_customer import get_customer_instructions
from assets.instruction_cashier import get_cashier_instructions
from assets.instruction_account_manager import get_account_manager_instructions


def main_menu():
    clear_screen()
    print_main(banner)
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
                clear_screen()
                print_content(get_customer_instructions(),"content")
                get_input("Press Enter",False,0.95)
                CustomerRole(user,encrypted_id).start()
        elif choice == "2":
            user,cashier_id = login_manager.login("cashier")
            if user:
                clear_screen()
                print_content(get_cashier_instructions(),"content")
                get_input("Press Enter",False,0.95)
                CashierRole(user,cashier_id).start()
        elif choice == "3":
            user,manager_id = login_manager.login("manager")
            if user:
                clear_screen()
                print_content(get_account_manager_instructions(),"content")
                get_input("Press Enter",False,0.95)
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

