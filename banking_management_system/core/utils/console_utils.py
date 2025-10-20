# core/utils/console_utils.py
import os
from core.utils.emoji import Emoji
from core.utils.color_utils import color_text, Color
from colorama import init as colorama_init


# from emoji import Emoji
# from color_utils import color_text, Color

# init colorama (helps Windows show ANSI colors)
colorama_init()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_header(title: str, line_count: int = 100):
    count = len(title)
    space = (line_count - count) // 2
    print(color_text("\n" + " " * 50 + "-" * line_count, Color.CYAN))
    print(
        color_text(
            " " * 50 + " " * space + f" {title.upper()} ", Color.BOLD + Color.BLUE
        )
    )
    print(color_text(" " * 50 + "-" * line_count, Color.CYAN))

def print_main(title: str, line_count: int = 100):
    count = len(title)
    space = (line_count - count) // 2
    print(color_text("\n" + " " * 50 + "=" * line_count, Color.ORANGE))
    print(
        color_text(
            " " * 50 + " " * space + f" {title.upper()} ", Color.BOLD + Color.ORANGE
        )
    )
    print(color_text(" " * 50 + "=" * line_count, Color.ORANGE))


def print_content(content: str, type_: str, indentation=0.55, resolution=100):
    type_ = type_.upper()
    if type_ == "SUCCESS":
        content = color_text(f" {content} ", Color.GREEN + Color.BOLD)
        content = " " * int(resolution * indentation) + Emoji.attach_emoji(
            content, "SUCCESS"
        )
        print(content)
    elif type_ == "ERROR":
        content = color_text(f" {content.upper()} ", Color.BOLD + Color.RED)
        content = " " * int(resolution * indentation) + Emoji.attach_emoji(
            content, "ERROR"
        )
        print(content)
    elif type_ == "WARNING":
        content = color_text(f" {content.upper()} ", Color.BOLD + Color.ORANGE)
        content = " " * int(resolution * indentation) + Emoji.attach_emoji(
            content, "WARNING"
        )
        print(content)
    elif type_ == "MONEY":
        content = color_text(f" {content.upper()} ", Color.GREEN)
        content = " " * int(resolution * indentation) + Emoji.attach_emoji(
            content, "MONEY"
        )
        print(content)
    elif type_ == "LOGIN":
        content = color_text(f" {content.upper()} ", Color.CYAN)
        content = " " * int(resolution * indentation) + Emoji.attach_emoji(
            content, "LOGIN"
        )
        print(content)
    elif type_ == "LOGOUT":
        content = color_text(f" {content.upper()} ", Color.BRIGHT_MAGENTA)
        content = " " * int(resolution * indentation) + Emoji.attach_emoji(
            content, "LOGOUT"
        )
        print(content)
    elif type_ == "USER":
        content = color_text(f" {content.upper()} ", Color.BRIGHT_MAGENTA)
        content = " " * int(resolution * indentation) + Emoji.attach_emoji(
            content, "USER"
        )
        print(content)
    elif type_ == "CLOCK":
        content = color_text(f" {content.upper()} ", Color.WHITE)
        content = " " * int(resolution * indentation) + Emoji.attach_emoji(
            content, "CLOCK"
        )
        print(content)
    elif type_ == "BANK":
        content = color_text(f" {content.upper()} ", Color.ORANGE)
        content = " " * int(resolution * indentation) + Emoji.attach_emoji(
            content, "BANK"
        )
        print(content)
    elif type_ == "INFO":
        content = color_text(f" {content.upper()} ", Color.WHITE)
        content = " " * int(resolution * indentation) + Emoji.attach_emoji(
            content, "INFO"
        )
        print(content)
    else:
        # fallback
        print(" " * int(resolution * indentation) +color_text(f" {content} ", Color.WHITE))


def get_input(prompt: str, required: bool = True,indentation=0.5, resolution=100) -> str:
    while True:
        value = input(color_text(" " * int(resolution * indentation)+f"{prompt}: ", Color.YELLOW))
        if not required or value.strip():
            return value.strip()
        print(" " * int(resolution*1.45 * indentation)+color_text("❌ Input cannot be empty. Try again!", Color.RED))


if __name__ == "__main__":
    print_header("Print a fancy colored section header")
    print_content("Operation OK", "SUCCESS")
    print_content("Something went wrong", "ERROR")
    print_content("This is a warning", "WARNING")
    print_content("Salary credited", "MONEY")
    print_content("User logged in", "LOGIN")
    print_content("User logged out", "LOGOUT")
    print_content("User info", "USER")
    print_content("Time stamp", "CLOCK")
    print_content("Bank", "BANK")
    print_content("General info", "INFO")
