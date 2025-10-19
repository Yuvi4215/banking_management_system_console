import json
import os
from datetime import datetime


class FileHelper:
    """
    Utility class for safe file handling (JSON read/write, backups, etc.)
    Keeps file management centralized for easier debugging and maintenance.
    """

    # -------------------------------------------------------------------------
    @staticmethod
    def ensure_directory_exists(file_path: str):
        """
        Ensure that the directory for a file exists.
        Creates missing folders automatically.
        """
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

    # -------------------------------------------------------------------------
    @staticmethod
    def read_json(file_path: str):
        """
        Safely read data from a JSON file.
        Returns an empty list or dict if file not found or empty.
        """
        try:
            if not os.path.exists(file_path):
                return []

            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read().strip()
                if not content:
                    return []
                return json.loads(content)
        except json.JSONDecodeError:
            print(
                f"⚠️ Warning: JSON decoding failed for file {file_path}. Returning empty data."
            )
            return []
        except Exception as e:
            print(f"❌ Error reading file {file_path}: {e}")
            return []

    # -------------------------------------------------------------------------
    @staticmethod
    def write_json(file_path: str, data):
        """
        Safely write data to a JSON file.
        Creates directories if they don’t exist.
        """
        try:
            FileHelper.ensure_directory_exists(file_path)
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"❌ Error writing to file {file_path}: {e}")

    # -------------------------------------------------------------------------
    @staticmethod
    def append_json(file_path: str, new_data):
        """
        Append a new record to a JSON list file.
        Automatically handles file creation if missing.
        """
        data = FileHelper.read_json(file_path)

        if not isinstance(data, list):
            print(f"⚠️ Warning: {file_path} is not a list-type JSON. Overwriting.")
            data = []

        data.append(new_data)
        FileHelper.write_json(file_path, data)

    # -------------------------------------------------------------------------
    @staticmethod
    def backup_file(file_path: str):
        """
        Create a timestamped backup copy of a file before major changes.
        Useful for transaction logs or account databases.
        """
        if not os.path.exists(file_path):
            return None

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{file_path}.backup_{timestamp}"
        try:
            with open(file_path, "r", encoding="utf-8") as src:
                with open(backup_path, "w", encoding="utf-8") as dst:
                    dst.write(src.read())
            return backup_path
        except Exception as e:
            print(f"⚠️ Backup failed for {file_path}: {e}")
            return None

    # -------------------------------------------------------------------------
    @staticmethod
    def delete_file(file_path: str):
        """
        Safely delete a file (used for admin maintenance or cleanup).
        """
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"🗑️ File deleted: {file_path}")
            else:
                print(f"⚠️ File not found: {file_path}")
        except Exception as e:
            print(f"❌ Error deleting file {file_path}: {e}")
