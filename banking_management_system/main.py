from core.utils.console_utils import clearScreen


def main_menu():
    clearScreen()
    print("=== 🏦 Banking Management System ===")
    print("1️⃣  Customer Login")
    print("2️⃣  Cashier Login")
    print("3️⃣  Account Manager Login")
    print("0️⃣  Exit")

def main():
    flag,attempt=True,0
    while flag:
        main_menu()
        choice = input("\nSelect an option: ")
        if choice == '1':
            print("Choice- 1")
            pass
        elif choice == '2':
            print("Choice- 2")
            pass
        elif choice == '3':
            print("Choice- 3")
            pass
        elif choice == '0':
            print("Logging out")
            flag=False
        else:
            print("❌ Invalid option. Try again.")
        
        if attempt>2:
            flag=False

if __name__ == "__main__":
    main()
