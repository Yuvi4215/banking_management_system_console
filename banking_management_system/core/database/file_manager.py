# core/database/file_manager.py
import json, os


class FileManager:

    def __init__(self, file_path):
        self.file_path = file_path
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        # Initialize file as empty dict if it does not exist
        if not os.path.exists(file_path):
            with open(file_path, "w") as fp:
                json.dump({}, fp, indent=4)
        else:
            # Validate JSON
            try:
                with open(file_path, "r") as fp:
                    data = json.load(fp)
                if not isinstance(data, dict):
                    raise ValueError
            except (json.JSONDecodeError, ValueError):
                with open(file_path, "w") as fp:
                    json.dump({}, fp, indent=4)

    def read_all(self):
        # print("in file manager- read all", self.file_path)
        with open(self.file_path, "r") as fp:
            return json.load(fp)
    
    def getCustomer(self, encrypted_id):
        data=self.read_all()
        return data[encrypted_id]

    def add_record(self, record: dict):
        """Merge a new record (dict) into the existing JSON dict."""
        data = self.read_all()
        data.update(record)  # Merge
        with open(self.file_path, "w") as fp:
            json.dump(data, fp, indent=4)

    def getEmployee(self, username):
        data = self.read_all()

        # Manager
        if username.lower() == "manager" and "manager" in data:
            print(data["manager"])
            return data["manager"]

        # Cashiers
        cashiers = data.get("cashier", [])
        for cashier in cashiers:
            if cashier.get("username") == username:
                print(cashier)
                return cashier  # return the dict, not a list

        return None

