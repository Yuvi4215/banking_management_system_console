
class Color:
    """ANSI color codes for beautiful console output."""

    RESET = "\033[0m"

    # Text colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BRIGHT_MAGENTA = "\033[95m"
    ORANGE = "\033[38;5;214m"

    # Styles
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def colorText(text, color):
    return f"{color}{text}{Color.RESET}"


if __name__=="__main__":
    print(colorText("name is just a name", Color.RED+Color.BOLD))



