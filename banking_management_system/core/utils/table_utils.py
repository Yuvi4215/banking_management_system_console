# core/utils/table_utils.py
from prettytable import PrettyTable
from core.utils.color_utils import color_text,Color
# from color_utils import color_text, Color

def create_table(
    headers, rows, title=None, resolution=100, indentation=30, colorize=True
):
    table = PrettyTable()
    if colorize:
        colored_headers = [
            color_text(head, Color.CYAN + Color.BOLD) for head in headers
        ]
        table.field_names = colored_headers
    else:
        table.field_names = headers

    for row in rows:
        colored_row = list(row)
        colored_row[0] = color_text(
            str(colored_row[0]), Color.BRIGHT_MAGENTA + Color.BOLD
        )
        table.add_row(colored_row)

    table.align = "c"
    table.border = True
    table.padding_width = 4

    if title:
        print(
            " " * int(indentation * 1.2)
            + color_text(f"📋 {title}\n", Color.BOLD + Color.YELLOW)
        )

    indent = " " * indentation
    print(indent + table.get_string().replace("\n", "\n" + indent))


if __name__ == "__main__":
    headers = ["Username", "Full Name", "Email", "Phone", "Address", "Account No"]
    dic = {'eaa99349': {'username': 'Ajay', 'full_name': 'Ajay Varma', 'email': 'ajay@example.com', 'phone': '+91-9999999999', 'address': '123 MG Road, Bangalore', 'account_no': 8187047}, '51e058f8': {'username': 'Sunny', 'full_name': 'Sunny Varma', 'email': 'sunny@example.com', 'phone': '+91-9988776655', 'address': '5 Fc Road, Pune', 'account_no': 2003963}, 'fdaa6e94': {'username': 'admin', 'full_name': 'Add min', 'email': 'add@min.com', 'phone': '9988776655', 'address': 'add Road, min', 'account_no': 9145179}}
    rows=[]
    for ele in dic.values():
        rows.append(ele.values())
    # print()
    create_table(headers, rows, title="Customer Accounts")
