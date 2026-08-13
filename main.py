from file_manager import FileManager
from history_manager import HistoryManager
from authentication import Authentication
from paper_manager import PaperManager
from recommendation_engine import RecommendationEngine
import pwinput
from favorite_manager import FavoriteManager
from admin import Admin
from user import User
from research_paper import ResearchPaper


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

                paper_obj = ResearchPaper(**paper)

                print("\n========== PAPER DETAILS ==========")
                paper_obj.display()

                if user is not None:

                    HistoryManager.add_history(
                        user["user_id"],
                        paper["paper_id"],
                        paper["title"]
                    )

                    print("\nPaper added to reading history.")

                    save = input(
                        "\nAdd this paper to favorites? (y/n): "
                    )

                    if save.lower() == "y":

                        FavoriteManager.add_favorite(

                            user["user_id"],
                            paper["paper_id"],
                            paper["title"]

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
                    print("Paper ID :", paper["paper_id"])
                    print("Title    :", paper["title"])
                    print("Author   :", paper["author"])
                    print("Category :", paper["category"])

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
                    print("Paper ID :", paper["paper_id"])
                    print("Title    :", paper["title"])
                    print("Author   :", paper["author"])
                    print("Category :", paper["category"])

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
                    print("Paper ID :", paper["paper_id"])
                    print("Title    :", paper["title"])
                    print("Author   :", paper["author"])
                    print("Category :", paper["category"])

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
                    print("Paper ID :", paper["paper_id"])
                    print("Title    :", paper["title"])
                    print("Author   :", paper["author"])
                    print("Category :", paper["category"])

        elif choice == "6":

            break

        else:

            print("Invalid choice.")


def admin_menu(admin_user):

    admin_obj = Admin(
        admin_user["user_id"],
        admin_user["username"],
        admin_user["password"]
    )

    while True:

        total_users = len(
            FileManager.read_csv(Authentication.USERS_FILE)
        )

        total_papers = len(
            PaperManager.get_all_papers()
        )

        print("\n==============================================")
        print("               ADMIN DASHBOARD")
        print("==============================================")
        print(f"Total Users           : {total_users}")
        print(f"Total Research Papers : {total_papers}")
        print("==============================================")

        print("\n========== ADMIN MENU ==========")
        print("1. Add Research Paper")
        print("2. View All Papers")
        print("3. Search Research Papers")
        print("4. View Users")
        print("5. Delete User")
        print("6. Retrain Recommendation Model")
        print("7. Logout")

        choice = input("Enter your choice: ")

        # --------------------------------------------------
        # ADD PAPER
        # --------------------------------------------------
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

            try:

                PaperManager.add_paper(paper)

                print("\nPaper added successfully.")

            except ValueError as error:

                print(error)

        # --------------------------------------------------
        # VIEW PAPERS
        # --------------------------------------------------
        elif choice == "2":

            papers = PaperManager.get_all_papers()

            if not papers:

                print("\nNo papers found.")

            else:

                print("\n" + "=" * 110)
                print(f"{'ID':<6}{'TITLE':<45}{'AUTHOR':<30}{'CATEGORY'}")
                print("=" * 110)

                for paper in papers:

                    print(
                        f"{paper['paper_id']:<6}"
                        f"{paper['title'][:42]:<45}"
                        f"{paper['author'][:27]:<30}"
                        f"{paper['category']}"
                    )

                print("=" * 110)
                print(f"Total Papers : {len(papers)}")

                paper_id = input(
                    "\nEnter Paper ID to view details (0 to go back): "
                )

                if paper_id != "0":

                    paper = PaperManager.get_paper_by_id(paper_id)

                    if paper:

                        paper_obj = ResearchPaper(**paper)

                        print("\n========== PAPER DETAILS ==========")
                        paper_obj.display()

                        print("\n1. Edit Paper")
                        print("2. Delete Paper")
                        print("3. Back")

                        admin_choice = input(
                            "Enter your choice: "
                        )

                        # ---------------- EDIT ----------------

                        if admin_choice == "1":

                            updated_paper = {

                                "paper_id": paper["paper_id"],

                                "title": input(
                                    f"Title [{paper['title']}]: "
                                ) or paper["title"],

                                "author": input(
                                    f"Author [{paper['author']}]: "
                                ) or paper["author"],

                                "category": input(
                                    f"Category [{paper['category']}]: "
                                ) or paper["category"],

                                "keywords": input(
                                    f"Keywords [{paper['keywords']}]: "
                                ) or paper["keywords"],

                                "abstract": input(
                                    f"Abstract [{paper['abstract']}]: "
                                ) or paper["abstract"],

                                "link": input(
                                    f"Link [{paper['link']}]: "
                                ) or paper["link"]

                            }

                            PaperManager.edit_paper(

                                paper["paper_id"],

                                updated_paper

                            )

                        # ---------------- DELETE ----------------

                        elif admin_choice == "2":

                            confirm = input(
                                "Are you sure? (Y/N): "
                            )

                            if confirm.lower() == "y":

                                PaperManager.delete_paper(
                                    paper["paper_id"]
                                )

                        # ---------------- BACK ----------------

                        elif admin_choice == "3":

                            pass

                        else:

                            print("Invalid choice.")

                    else:

                        print("Invalid Paper ID.")

        # --------------------------------------------------
        # SEARCH
        # --------------------------------------------------
        elif choice == "3":

            search_menu()

        # --------------------------------------------------
        # VIEW USERS
        # --------------------------------------------------
        elif choice == "4":

            users = FileManager.read_csv(
                Authentication.USERS_FILE
            )

            print("\n========== USERS ==========")

            for user in users:

                print("-" * 40)

                print("User ID  :", user["user_id"])
                print("Username :", user["username"])
                print("Role     :", user["role"])
                print("Interest :", user["interest"])

        # --------------------------------------------------
        # DELETE USER
        # --------------------------------------------------
        elif choice == "5":

            user_id = input(
                "Enter User ID to delete: "
            )

            confirm = input(
                "Are you sure? (Y/N): "
            )

            if confirm.lower() == "y":

                users = FileManager.read_csv(
                    Authentication.USERS_FILE
                )

                updated_users = [

                    user

                    for user in users

                    if user["user_id"] != user_id

                ]

                FileManager.write_csv(

                    Authentication.USERS_FILE,

                    Authentication.USER_FIELDS,

                    updated_users

                )

                print("\nUser deleted successfully.")

            else:

                print("\nDeletion cancelled.")

        # --------------------------------------------------
        # RETRAIN RECOMMENDATION MODEL
        # --------------------------------------------------
        elif choice == "6":

            confirm = input(
                "\nThis will retrain the model on the current "
                "papers.csv. Continue? (Y/N): "
            )

            if confirm.lower() == "y":

                admin_obj.retrain_model()

                RecommendationEngine.reload_model()

                print("The running app is now using the updated model.")

            else:

                print("\nRetraining cancelled.")

        # --------------------------------------------------
        # LOGOUT
        # --------------------------------------------------
        elif choice == "7":

            print("\n========================================")
            print("Administrator logged out successfully.")
            print("========================================")

            break

        else:

            print("Invalid choice.")

def user_menu(user):

    while True:

        total_papers = len(PaperManager.get_all_papers())

        print("\n==============================================")
        print(f"Welcome, {user['username']}")
        print(f"Research Interest : {user['interest']}")
        print(f"Total Papers Available : {total_papers}")
        print("==============================================")

        print(f"\n========== USER MENU ({user['username']}) ==========")
        print("1. View All Papers")
        print("2. Search Papers")
        print("3. Get AI Recommendations")
        print("4. View Reading History")
        print("5. View Favorite Papers")
        print("6. Remove Favorite Paper")
        print("7. Update Research Interest")
        print("8. Logout")

        choice = input("Enter your choice: ").strip()

        # =====================================================
        # VIEW ALL PAPERS
        # =====================================================

        if choice == "1":

            papers = PaperManager.get_all_papers()

            if not papers:

                print("\nNo papers found.")
                input("\nPress Enter to continue...")
                continue

            print("\n" + "=" * 110)
            print(f"{'ID':<6}{'TITLE':<45}{'AUTHOR':<30}{'CATEGORY'}")
            print("=" * 110)

            for paper in papers:

                print(
                    f"{paper['paper_id']:<6}"
                    f"{paper['title'][:42]:<45}"
                    f"{paper['author'][:27]:<30}"
                    f"{paper['category']}"
                )

            print("=" * 110)
            print(f"Total Papers : {len(papers)}")

            paper_id = input(
                "\nEnter Paper ID to view full details (0 to go back): "
            )

            if paper_id == "0":
                continue

            paper = PaperManager.get_paper_by_id(paper_id)

            if paper is None:

                print("\nInvalid Paper ID.")
                input("\nPress Enter to continue...")
                continue

            paper_obj = ResearchPaper(**paper)

            print("\n========== PAPER DETAILS ==========")
            paper_obj.display()

            HistoryManager.add_history(
                user["user_id"],
                paper["paper_id"],
                paper["title"]
            )

            save = input(
                "\nAdd this paper to favorites? (Y/N): "
            )

            if save.lower() == "y":

                FavoriteManager.add_favorite(
                    user["user_id"],
                    paper["paper_id"],
                    paper["title"]
                )

            input("\nPress Enter to continue...")

        # =====================================================
        # SEARCH
        # =====================================================

        elif choice == "2":

            search_menu(user)
            input("\nPress Enter to continue...")

        # =====================================================
        # AI RECOMMENDATION
        # =====================================================

        elif choice == "3":

            recommendations = RecommendationEngine.recommend(user)

            if not recommendations:

                print("\nNo recommendations found.")
                print(f"We predicted your top interest as: {RecommendationEngine.last_predicted_category}")
                print("But there are no unread papers left in the categories we checked:")

                for category, score in RecommendationEngine.last_attempted_categories:
                    print(f"  - {category} ({score:.2f}% confidence)")

                input("\nPress Enter to continue...")
                continue

            print("\n========== AI RECOMMENDATIONS ==========")

            for paper in recommendations:

                print("-" * 60)
                print("Paper ID :", paper["paper_id"])
                print("Title    :", paper["title"])
                print("Author   :", paper["author"])
                print("Category :", paper["category"])
                print("Keywords :", paper["keywords"])
                print(f"Recommendation Score : {paper['score']:.2f}%")
                print("\nReason:")
                for r in paper["reason"]:
                    print(f"✓ {r}")
                print("\nLink :", paper["link"])

            save = input(
                "\nWould you like to save a paper to favorites? (Y/N): "
            )

            if save.lower() == "y":

                paper_id = input("Enter Paper ID: ")

                found = False

                for paper in recommendations:

                    if str(paper["paper_id"]) == paper_id:

                        FavoriteManager.add_favorite(
                            user["user_id"],
                            paper["paper_id"],
                            paper["title"]
                        )

                        found = True
                        break

                if not found:
                    print("\nInvalid Paper ID.")

            input("\nPress Enter to continue...")

        # =====================================================
        # HISTORY
        # =====================================================

        elif choice == "4":

            HistoryManager.view_user_history(
                user["user_id"]
            )

            input("\nPress Enter to continue...")

        # =====================================================
        # FAVORITES
        # =====================================================

        elif choice == "5":

            FavoriteManager.view_favorites(
                user["user_id"]
            )

            input("\nPress Enter to continue...")

        # =====================================================
        # REMOVE FAVORITE
        # =====================================================

        elif choice == "6":

            paper_id = input("Enter Paper ID to remove: ")

            FavoriteManager.remove_favorite(
                user["user_id"],
                paper_id
            )

            input("\nPress Enter to continue...")

        # =====================================================
        # UPDATE RESEARCH INTEREST
        # =====================================================

        elif choice == "7":

            print(f"\nCurrent Research Interest: {user['interest']}")

            new_interest = input(
                "Enter new research interest: "
            ).strip()

            if not new_interest:

                print("\nInterest cannot be empty. No changes made.")

            else:

                user_obj = User(
                    user["user_id"],
                    user["username"],
                    user["password"],
                    user["interest"]
                )

                user_obj.update_interest(new_interest)

                Authentication.update_interest(
                    user["user_id"],
                    user_obj.interest
                )

                # Keep this session's dict in sync so the dashboard
                # and future recommendations use the new interest
                # without requiring a re-login.
                user["interest"] = user_obj.interest

                print("\nResearch interest updated successfully.")

            input("\nPress Enter to continue...")

        # =====================================================
        # LOGOUT
        # =====================================================

        elif choice == "8":

            print("\n========================================")
            print("You have been logged out successfully.")
            print("Thank you for using the")
            print("Research Paper Recommendation System.")
            print("========================================")

            break

        else:

            print("\nInvalid choice. Please try again.")

def register():

    print("\n===== REGISTER =====")

    user_id = input("User ID: ")
    username = input("Username: ")

    password = pwinput.pwinput(prompt="Password: ")
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

    while True:

        print("\n===== LOGIN =====")

        username = input("Username: ")

        password = pwinput.pwinput(prompt="Password: ")

        user = Authentication.login(username, password)

        if user is None:

            print("\nInvalid username or password.")

            choice = input(
                "Try again? (Y/N): "
            )

            if choice.lower() != "y":
                return

            continue

        if user["role"].lower() == "admin":
            admin_menu(user)
        else:
            user_menu(user)

        break

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
            print("\n==============================================")
            print(" Thank you for using")
            print(" Research Paper Recommendation System")
            print("")
            print(" We hope to see you again!")
            print(" Goodbye!")
            print("==============================================")

            break
        else:
            print(
                "Invalid choice."
            )
if __name__ == "__main__":
    main()
