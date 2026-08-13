from file_manager import FileManager
import os


class FavoriteManager:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    FAVORITES_FILE = os.path.join(
        BASE_DIR,
        "data",
        "favorites.csv"
    )

    FAVORITE_FIELDS = [
        "user_id",
        "paper_id",
        "title"
    ]

    @classmethod
    def add_favorite(cls, user_id, paper_id, title):

        favorites = FileManager.read_csv(cls.FAVORITES_FILE)

        # Prevent duplicate favourites
        for favorite in favorites:

            if (
                favorite["user_id"] == str(user_id)
                and favorite["paper_id"] == str(paper_id)
            ):
                print("\nThis paper is already in your favourites.")
                return False

        new_favorite = {
            "user_id": str(user_id),
            "paper_id": str(paper_id),
            "title": title
        }

        FileManager.append_csv(
            cls.FAVORITES_FILE,
            cls.FAVORITE_FIELDS,
            new_favorite
        )

        print("\nPaper added to favourites successfully.")
        return True

    @classmethod
    def view_favorites(cls, user_id):

        favorites = FileManager.read_csv(cls.FAVORITES_FILE)

        user_favorites = [
            favorite
            for favorite in favorites
            if favorite["user_id"] == str(user_id)
        ]

        if not user_favorites:
            print("\nNo favourite papers found.")
            return

        print("\n" + "=" * 70)
        print("                 MY FAVOURITE PAPERS")
        print("=" * 70)
        print(f"{'Paper ID':<12}{'Title'}")
        print("-" * 70)

        for favorite in user_favorites:
            print(
                f"{favorite['paper_id']:<12}"
                f"{favorite['title']}"
            )

        print("=" * 70)
        print(f"Total Favourite Papers : {len(user_favorites)}")

    @classmethod
    def remove_favorite(cls, user_id, paper_id):

        favorites = FileManager.read_csv(cls.FAVORITES_FILE)

        found = False

        updated_favorites = []

        for favorite in favorites:

            if (
                favorite["user_id"] == str(user_id)
                and favorite["paper_id"] == str(paper_id)
            ):
                found = True
                continue

            updated_favorites.append(favorite)

        if not found:
            print("\nPaper not found in your favourites.")
            return False

        FileManager.write_csv(
            cls.FAVORITES_FILE,
            cls.FAVORITE_FIELDS,
            updated_favorites
        )

        print("\nFavourite removed successfully.")
        return True