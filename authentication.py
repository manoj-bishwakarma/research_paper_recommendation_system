from file_manager import FileManager


class Authentication:
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    USERS_FILE = os.path.join(BASE_DIR, "data", "users.csv")
    USER_FIELDS = [
        "user_id",
        "username",
        "password",
        "role",
        "interest"
    ]

    @classmethod
    def register(cls, user_id, username, password, role, interest):
        users = FileManager.read_csv(cls.USERS_FILE)

        for user in users:
            if user["username"] == username:
                raise ValueError("Username already exists.")

        new_user = {
            "user_id": user_id,
            "username": username,
            "password": password,
            "role": role,
            "interest": interest
        }

        FileManager.append_csv(
            cls.USERS_FILE,
            cls.USER_FIELDS,
            new_user
        )

        return True

    @classmethod
    def login(cls, username, password):
        users = FileManager.read_csv(cls.USERS_FILE)

        for user in users:
            if (
                user["username"] == username
                and user["password"] == password
            ):
                return user

        return None