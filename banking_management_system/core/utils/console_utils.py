import os
from emoji import Emoji
from color_utils import colorText, Color

# from core.utils.emoji import Emoji
# from core.utils.color_utils import colorText, Color


def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


def printHeader(title, resolution=100):
    """Print a fancy colored section header"""

    line_count = 100
    count = len(title)
    space = (line_count - count) // 2
    print(colorText("\n" + " " * 50 + "=" * line_count, Color.CYAN))
    print(
        colorText(
            " " * 50 + " " * space + f" {title.upper()} ", Color.BOLD + Color.BLUE
        )
    )
    print(colorText(" " * 50 + "=" * line_count, Color.CYAN))


def printContent(containt: str, type: str,indentaton=0.55, resolution=100):
    if type == "SUCCESS":
        containt = colorText(f" {containt} ", Color.GREEN+ Color.BOLD)
        containt = " " * int(resolution * indentaton) + Emoji.attachEmoji(containt, "SUCCESS")
        print(containt)

    elif type == "ERROR":
        containt = colorText(f" {containt.upper()} ", Color.BOLD + Color.RED)
        containt = " " * int(resolution * indentaton) + Emoji.attachEmoji(containt, "ERROR")
        print(containt)

    elif type == "WARNING":
        containt = colorText(f" {containt.upper()} ", Color.BOLD + Color.ORANGE)
        containt = " " * int(resolution * indentaton) + Emoji.attachEmoji(containt, "WARNING")
        print(containt)

    elif type == "MONEY":
        containt = colorText(f" {containt.upper()} ", Color.GREEN)
        containt = " " * int(resolution * indentaton) + Emoji.attachEmoji(containt, "MONEY")
        print(containt)
        
    elif type == "LOGIN":
        containt = colorText(f" {containt.upper()} ", Color.CYAN)
        containt = " " * int(resolution * indentaton) + Emoji.attachEmoji(containt, "LOGIN")
        print(containt)
        
    elif type == "LOGOUT":
        containt = colorText(f" {containt.upper()} ", Color.BRIGHT_MAGENTA)
        containt = " " * int(resolution * indentaton) + Emoji.attachEmoji(containt, "LOGOUT")
        print(containt)
        
    elif type == "USER":
        containt = colorText(f" {containt.upper()} ", Color.BRIGHT_MAGENTA)
        containt = " " * int(resolution * indentaton) + Emoji.attachEmoji(containt, "USER")
        print(containt)
        
    elif type == "CLOCK":
        containt = colorText(f" {containt.upper()} ", Color.WHITE)
        containt = " " * int(resolution * indentaton) + Emoji.attachEmoji(containt, "CLOCK")
        print(containt)
     
    elif type=="BANK":
        containt = colorText(f" {containt.upper()} ", Color.ORANGE)
        containt = " " * int(resolution * indentaton) + Emoji.attachEmoji(containt, "BANK")
        print(containt)

    elif type == "INFO":
        containt = colorText(f" {containt.upper()} ", Color.WHITE)
        containt = " " * int(resolution * indentaton) + Emoji.attachEmoji(containt, "INFO")
        print(containt)
   
    else:
        pass



def getInput(prompt, required=True):
    """Safely get user input (with validation for empty inputs)"""
    while True:
        value = input(colorText(f"{prompt}: ", Color.YELLOW))
        if not required or value.strip():
            return value.strip()
        print(colorText("❌ Input cannot be empty. Try again!", Color.RED))


if __name__ == "__main__":
    printHeader("Print a fancy colored section header")
    printContent("Print SUCCESSr", "SUCCESS")
    printContent("Print ERROR", "ERROR")
    printContent("Print WARNING", "WARNING")
    printContent("Print MONEY", "MONEY")
    printContent("Print LOGIN", "LOGIN")
    printContent("Print LOGOUT", "LOGOUT")
    printContent("Print USER", "USER")
    printContent("Print CLOCK", "CLOCK")
    printContent("Print BANK", "BANK")
    printContent("Print INFO", "INFO")
        # getInput("Enter the Input ", False)
