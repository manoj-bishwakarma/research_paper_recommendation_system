import os

print("Current working directory:", os.getcwd())

from history_manager import HistoryManager
from authentication import Authentication
from paper_manager import PaperManager
from recommendation_engine import RecommendationEngine



def search_menu(user=None):

    while True:

        print("\n========== SEARCH MENU ==========")
        print("1. View Paper Details by ID")
        print("2. Search by Title")
        print("3. Search by Author")
        print("4. Search by Category")
        print("5. Search by Keyword")
        print("6. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            paper_id = input("Enter Paper ID: ")

            paper = PaperManager.get_paper_by_id(
                paper_id
            )

            if paper is None:

                print("Paper not found.")

            else:

                print("\n========== PAPER DETAILS ==========")

                print("Paper ID :", paper["paper_id"])
                print("Title    :", paper["title"])
                print("Author   :", paper["author"])
                print("Category :", paper["category"])
                print("Keywords :", paper["keywords"])
                print("Abstract :", paper["abstract"])
                print("Link     :", paper["link"])

                # Save reading history only for logged-in users
                if user is not None:

                    HistoryManager.add_history(
                        user["user_id"],
                        paper["paper_id"],
                        paper["title"]
                    )

                    print(
                        "\nPaper added to reading history."
                    )

        elif choice == "2":

            title = input("Enter title: ")

            results = PaperManager.search_by_title(
                title
            )

            if not results:

                print("No papers found.")

            else:

                for paper in results:

                    print("-" * 50)
                    print("ID:", paper["paper_id"])
                    print("Title:", paper["title"])
                    print("Author:", paper["author"])
                    print("Category:", paper["category"])

        elif choice == "3":

            author = input("Enter author: ")

            results = PaperManager.search_by_author(
                author
            )

            if not results:

                print("No papers found.")

            else:

                for paper in results:

                    print("-" * 50)
                    print("ID:", paper["paper_id"])
                    print("Title:", paper["title"])
                    print("Author:", paper["author"])
                    print("Category:", paper["category"])

        elif choice == "4":

            category = input("Enter category: ")

            results = PaperManager.search_by_category(
                category
            )

            if not results:

                print("No papers found.")

            else:

                for paper in results:

                    print("-" * 50)
                    print("ID:", paper["paper_id"])
                    print("Title:", paper["title"])
                    print("Author:", paper["author"])
                    print("Category:", paper["category"])

        elif choice == "5":

            keyword = input("Enter keyword: ")

            results = PaperManager.search_by_keyword(
                keyword
            )

            if not results:

                print("No papers found.")

            else:

                for paper in results:

                    print("-" * 50)
                    print("ID:", paper["paper_id"])
                    print("Title:", paper["title"])
                    print("Author:", paper["author"])
                    print("Category:", paper["category"])

        elif choice == "6":

            break

        else:

            print("Invalid choice.")
def admin_menu():

    while True:

        print("\n========== ADMIN MENU ==========")
        print("1. Add Research Paper")
        print("2. View All Papers")
        print("3. Edit Research Paper")
        print("4. Delete Research Paper")
        print("5. Search Research Papers")
        print("6. View Users")
        print("7. Delete User")
        print("8. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":

            paper = {
                "paper_id": input("Paper ID: "),
                "title": input("Title: "),
                "author": input("Author: "),
                "category": input("Category: "),
                "keywords": input("Keywords: "),
                "abstract": input("Abstract: "),
                "link": input("Paper Link: ")
            }

            PaperManager.add_paper(paper)

            print("Paper added successfully.")

        elif choice == "2":

            papers = PaperManager.get_all_papers()

            if not papers:
                print("No papers found.")

            else:

                for paper in papers:

                    print("-" * 50)

                    print("ID:", paper["paper_id"])
                    print("Title:", paper["title"])
                    print("Author:", paper["author"])
                    print("Category:", paper["category"])
                    print("Keywords:", paper["keywords"])

        elif choice == "3":

            paper_id = input(
                "Enter Paper ID to edit: "
            )

            updated_paper = {

                "paper_id": paper_id,
                "title": input("New Title: "),
                "author": input("New Author: "),
                "category": input("New Category: "),
                "keywords": input("New Keywords: "),
                "abstract": input("New Abstract: "),
                "link": input("New Link: ")

            }

            PaperManager.edit_paper(
                paper_id,
                updated_paper
            )

        elif choice == "4":

            paper_id = input(
                "Enter Paper ID to delete: "
            )

            PaperManager.delete_paper(
                paper_id
            )

        elif choice == "5":

            search_menu()

        elif choice == "6":

            users = Authentication.login.__self__.read_csv \
                if False else None

            from file_manager import FileManager

            users = FileManager.read_csv(
                Authentication.USERS_FILE
            )

            for user in users:

                print("-" * 40)

                print(
                    "User ID:",
                    user["user_id"]
                )

                print(
                    "Username:",
                    user["username"]
                )

                print(
                    "Role:",
                    user["role"]
                )

                print(
                    "Interest:",
                    user["interest"]
                )

        elif choice == "7":

            from file_manager import FileManager

            user_id = input(
                "Enter User ID to delete: "
            )

            users = FileManager.read_csv(
                Authentication.USERS_FILE
            )

            updated_users = [

                user

                for user in users

                if user["user_id"]
                != user_id

            ]

            FileManager.write_csv(
                Authentication.USERS_FILE,
                Authentication.USER_FIELDS,
                updated_users
            )

            print(
                "User deleted successfully."
            )

        elif choice == "8":

            break

        else:

            print("Invalid choice.")


def user_menu(user):

    while True:

        print(
            f"\n========== USER MENU ({user['username']}) =========="
        )

        print("1. View All Papers")
        print("2. Search Papers")
        print("3. Get AI Recommendations")
        print("4. View Reading History")
        print("5. Logout")

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            papers = (
                PaperManager.get_all_papers()
            )

            if not papers:

                print("No papers found.")

            else:

                for paper in papers:

                    print("-" * 40)

                    print(
                        "ID:",
                        paper["paper_id"]
                    )

                    print(
                        "Title:",
                        paper["title"]
                    )

                    print(
                        "Author:",
                        paper["author"]
                    )

                    print(
                        "Category:",
                        paper["category"]
                    )

        elif choice == "2":

            search_menu(user)

        elif choice == "3":

            papers = (
                PaperManager.get_all_papers()
            )

            recommendations = (
                RecommendationEngine.recommend(
                    user["interest"],
                    papers
                )
            )

            if not recommendations:

                print(
                    "No recommendations found."
                )

            else:

                print(
                    "\nRecommended Papers:"
                )

                for paper in recommendations:

                    print("-" * 40)

                    print(
                        "Title:",
                        paper["title"]
                    )

                    print(
                        "Author:",
                        paper["author"]
                    )

                    print(
                        "Category:",
                        paper["category"]
                    )

        elif choice == "4":

            HistoryManager.view_user_history(
                user["user_id"]
            )
        elif choice == "5":

            break

        else:

            print("Invalid choice.")


def register():

    print("\n===== REGISTER =====")

    user_id = input("User ID: ")
    username = input("Username: ")
    password = input("Password: ")
    role = input("Role (Admin/User): ")
    interest = input("Research Interest: ")

    try:

        Authentication.register(
            user_id=user_id,
            username=username,
            password=password,
            role=role,
            interest=interest
        )

        print(
            "Registration successful."
        )

    except ValueError as error:

        print(error)


def login():

    print("\n===== LOGIN =====")

    username = input("Username: ")
    password = input("Password: ")

    user = Authentication.login(
        username,
        password
    )

    if user is None:

        print(
            "Invalid username or password."
        )

        return

    if (
        user["role"].lower()
        == "admin"
    ):

        admin_menu()

    else:

        user_menu(user)


def main():

    while True:

        print(
            "\n========== RESEARCH PAPER RECOMMENDATION SYSTEM =========="
        )

        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            register()

        elif choice == "2":

            login()

        elif choice == "3":

            print("Goodbye!")
            break

        else:

            print(
                "Invalid choice."
            )


if __name__ == "__main__":
    main()

