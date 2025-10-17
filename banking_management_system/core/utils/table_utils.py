# core/utils/table_utils.py
from prettytable import PrettyTable
from core.utils.color_utils import color_text, Color
# from color_utils import color_text, Color

def create_table(
    headers, rows, title=None, resolution=100, indentation=70, colorize=True
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
    headers = ["Account No", "Name", "Balance (₹)"]
    rows = [
        ["1001", "Thor", "5000"],
        ["1002", "Ironman", "3200"],
        ["1003", "Ninja", "8700"],
    ]
    create_table(headers, rows, title="Customer Accounts")
