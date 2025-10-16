class Emoji:
    """Common emoji shortcuts used across the app"""

    SUCCESS = "✅"
    ERROR = "❌"
    WARNING = "⚠️"
    MONEY = "💰"
    LOGIN = "🔐"
    LOGOUT = "🚪"
    USER = "👤"
    CLOCK = "🕒"
    BANK = "🏦"
    INFO = "ℹ️"

    @staticmethod
    def attachEmoji(content: str, emoji_type: str) -> str:
        # Convert to uppercase to make lookup case-insensitive
        emoji_type = emoji_type.upper()
        
        # Check if the emoji type exists as a class attribute
        if hasattr(Emoji, emoji_type):
            emoji = getattr(Emoji, emoji_type)
            return f"{emoji} {content}"
        else:
            return f"❓ {content}"

if __name__=="__main__":
    print(Emoji.attachEmoji("Login successful", "success"))
    # Output: ✅ Login successful

    print(Emoji.attachEmoji("Something went wrong", "error"))
    # Output: ❌ Something went wrong

    print(Emoji.attachEmoji("Unknown type example", "notfound"))


