class User:

    def __init__(self, username, password, role):
        self._username = username
        self._password = password
        self._role = role.upper()

    # --- Encapsulation (getters and setters) ---
    def get_username(self):
        return self._username

    def get_role(self):
        return self._role


    def __str__(self):
        return f"{self._role} {self._username}"


if __name__=="__main__":
    u1=User("101","password", "Manager")
    print(u1)