# core/utils/emoji.py
class Emoji:
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
    def attach_emoji(content: str, emoji_type: str) -> str:
        emoji_type = emoji_type.upper()
        if hasattr(Emoji, emoji_type):
            emoji = getattr(Emoji, emoji_type)
            return f"{emoji} {content}"
        else:
            return f"❓ {content}"

if __name__ == "__main__":
    print(Emoji.attach_emoji("Login successful", "success"))
