from file_manager import FileManager
import hashlib
import os


class Authentication:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    USERS_FILE = os.path.join(BASE_DIR, "data", "users.csv")

    USER_FIELDS = [
        "user_id",
        "username",
        "password",
        "role",
        "interest"
    ]

    @staticmethod
    def hash_password(password):
        """
        Convert plain text password to SHA-256 hash.
        """
        return hashlib.sha256(
            password.encode("utf-8")
        ).hexdigest()

    @classmethod
    def register(cls, user_id, username, password, role, interest):
        """
        Register a new user.
        Checks duplicate User ID and Username.
        """

        users = FileManager.read_csv(cls.USERS_FILE)

        for user in users:

            # Check duplicate User ID
            if user["user_id"] == user_id:
                raise ValueError("User ID already exists.")

            # Check duplicate Username (case-insensitive)
            if user["username"].lower() == username.lower():
                raise ValueError("Username already exists.")

        new_user = {

            "user_id": user_id,
            "username": username,
            "password": cls.hash_password(password),
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
        """
        Authenticate user.
        """

        users = FileManager.read_csv(cls.USERS_FILE)

        hashed_password = cls.hash_password(password)

        for user in users:

            if (
                user["username"].lower() == username.lower()
                and user["password"] == hashed_password
            ):
                return user

        return None

    @classmethod
    def update_interest(cls, user_id, new_interest):

        users = FileManager.read_csv(cls.USERS_FILE)

        found = False

        for user in users:

            if user["user_id"] == str(user_id):

                user["interest"] = new_interest
                found = True
                break

        if not found:
            raise ValueError("User not found.")

        FileManager.write_csv(
            cls.USERS_FILE,
            cls.USER_FIELDS,
            users
        )

        return True
