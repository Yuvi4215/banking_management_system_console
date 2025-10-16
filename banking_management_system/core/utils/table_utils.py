from prettytable import PrettyTable
# from color_utils import colorText, Color
from core.utils.color_utils import colorText, Color


def create_table(headers, rows, title=None, colorize=True):
    """
    Create and print a PrettyTable with optional colored headers and magenta first column.

    Args:
        headers (list): Column headers
        rows (list[list]): Data rows
        title (str): Optional table title
        colorize (bool): Whether to apply ANSI colors
    """
    table = PrettyTable()

    # Colorize headers if enabled
    if colorize:
        colored_headers = [colorText(head, Color.CYAN + Color.BOLD) for head in headers]
        table.field_names = colored_headers
    else:
        table.field_names = headers

    # Add colored rows
    for row in rows:
        colored_row = row.copy()

        # Apply bright magenta color to first column only
        colored_row[0] = colorText(str(colored_row[0]), Color.BRIGHT_MAGENTA + Color.BOLD)

        table.add_row(colored_row)

    # Styling
    table.align = "c"
    table.border = True
    table.padding_width = 4

    # Optional title
    if title:
        print(colorText(f"\n📋 {title}\n", Color.BOLD + Color.YELLOW))

    print(table)

# def center_text(text, width=50):
#     """Center align text for banners or messages."""
#     return text.center(width)


if __name__=="__main__":
    headers = ["Account No", "Name", "Balance (₹)"]
rows = [
    ["1001", "Thor", "5000"],
    ["1002", "Ironman", "3200"],
    ["1003", "Ninja", "8700"],
]

create_table(headers, rows, title="Customer Accounts")
