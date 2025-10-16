# from core.utils.console_utils import clearScreen


# def main_menu():
#     clearScreen()
#     print("=== 🏦 Banking Management System ===")
#     print("1️⃣  Customer Login")
#     print("2️⃣  Cashier Login")
#     print("3️⃣  Account Manager Login")
#     print("0️⃣  Exit")

# def main():
#     flag,attempt=True,0
#     while flag:
#         main_menu()
#         choice = input("\nSelect an option: ")
#         if choice == '1':
#             print("Choice- 1")
#             pass
#         elif choice == '2':
#             print("Choice- 2")
#             pass
#         elif choice == '3':
#             print("Choice- 3")
#             pass
#         elif choice == '0':
#             print("Logging out")
#             flag=False
#         else:
#             attempt+=1
#             print("❌ Invalid option. Try again.")
#             print(f"Attempt number : {attempt} failed")
#         if attempt>2:
#             flag=False
#     print("Program terminated....")

# if __name__ == "__main__":
#     main()

# test_utils.py (place at banking_management_system/)
from core.utils.console_utils import print_header, print_content
from core.utils.table_utils import create_table
from core.utils.timestamp_utils import get_timestamp

def main():
    print_header("Utils Test")
    print_content("All systems go", "SUCCESS")
    headers = ["ID","Name","Balance"]
    rows = [[1,"Alice","₹5000"], [2,"Bob","₹3000"]]
    create_table(headers, rows, title="Accounts")
    print("Timestamp:", get_timestamp())

if __name__ == "__main__":
    main()

