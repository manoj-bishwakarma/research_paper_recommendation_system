from file_manager import FileManager
import os



class HistoryManager:

    BASE_DIR = os.path.dirname(
        os.path.abspath(__file__)
    )

    HISTORY_FILE = os.path.join(
        BASE_DIR,
        "data",
        "history.csv"
    )

    HISTORY_FIELDS = [
        "user_id",
        "paper_id",
        "title"
    ]

    @classmethod
    def add_history(cls, user_id, paper_id, title):

        history_record = {
            "user_id": str(user_id),
            "paper_id": str(paper_id),
            "title": title
        }

        FileManager.append_csv(
            cls.HISTORY_FILE,
            cls.HISTORY_FIELDS,
            history_record
        )

    @classmethod
    def get_user_history(
            cls,
            user_id
    ):

        history = FileManager.read_csv(
            cls.HISTORY_FILE
        )

        return [

            record

            for record in history

            if record["user_id"]
            == str(user_id)

        ]

    @classmethod
    def view_user_history(
            cls,
            user_id
    ):

        history = cls.get_user_history(
            user_id
        )

        if not history:

            print(
                "No reading history found."
            )

            return

        print(
            "\n========== READING HISTORY =========="
        )

        for record in history:

            print("-" * 40)

            print(
                "Paper ID:",
                record["paper_id"]
            )

            print(
                "Title:",
                record["title"]
            )

    @classmethod
    def clear_user_history(
            cls,
            user_id
    ):

        history = FileManager.read_csv(
            cls.HISTORY_FILE
        )

        updated_history = [

            record

            for record in history

            if record["user_id"]
            != str(user_id)

        ]

        FileManager.write_csv(
            cls.HISTORY_FILE,
            cls.HISTORY_FIELDS,
            updated_history
        )

        print(
            "History cleared successfully."
        )