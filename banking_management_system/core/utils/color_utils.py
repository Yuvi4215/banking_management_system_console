# core/utils/color_utils.py
class Color:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BRIGHT_MAGENTA = "\033[95m"
    ORANGE = "\033[38;5;214m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def color_text(text: str, color: str) -> str:
    return f"{color}{text}{Color.RESET}"


if __name__ == "__main__":
    print(color_text("name is just a name", Color.RED + Color.BOLD))
    print(color_text("name is just a name", Color.GREEN + Color.BOLD))
    print(color_text("name is just a name", Color.YELLOW + Color.BOLD))
    print(color_text("name is just a name", Color.BLUE + Color.BOLD))
    print(color_text("name is just a name", Color.CYAN + Color.BOLD))