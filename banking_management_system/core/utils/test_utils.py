# test_utils.py (place at banking_management_system/)
from core.utils.console_utils import print_header, print_content
from core.utils.table_utils import create_table
from core.utils.timestamp_utils import get_timestamp


def main():
    print_header("Utils Test")
    print_content("All systems go", "SUCCESS")
    headers = ["ID", "Name", "Balance"]
    rows = [[1, "Alice", "₹5000"], [2, "Bob", "₹3000"]]
    create_table(headers, rows, title="Accounts")
    print("Timestamp:", get_timestamp())


if __name__ == "__main__":
    main()
