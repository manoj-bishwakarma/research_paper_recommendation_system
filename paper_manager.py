from file_manager import FileManager
import os


class PaperManager:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PAPERS_FILE = os.path.join(BASE_DIR, "data", "papers.csv")

    PAPER_FIELDS = [
        "paper_id",
        "title",
        "author",
        "category",
        "keywords",
        "abstract",
        "link"
    ]

    @classmethod
    def add_paper(cls, paper):
        FileManager.append_csv(
            cls.PAPERS_FILE,
            cls.PAPER_FIELDS,
            paper
        )

    @classmethod
    def get_all_papers(cls):
        return FileManager.read_csv(
            cls.PAPERS_FILE
        )

    @classmethod
    def get_paper_by_id(cls, paper_id):

        papers = cls.get_all_papers()

        for paper in papers:

            if paper["paper_id"] == str(paper_id):

                return paper

        return None

    @classmethod
    def search_by_title(cls, title):

        papers = cls.get_all_papers()

        return [
            paper
            for paper in papers
            if title.lower()
            in paper["title"].lower()
        ]

    @classmethod
    def search_by_author(cls, author):

        papers = cls.get_all_papers()

        return [
            paper
            for paper in papers
            if author.lower()
            in paper["author"].lower()
        ]

    @classmethod
    def search_by_category(cls, category):

        papers = cls.get_all_papers()

        return [
            paper
            for paper in papers
            if category.lower()
            == paper["category"].lower()
        ]

    @classmethod
    def search_by_keyword(cls, keyword):

        papers = cls.get_all_papers()

        return [
            paper
            for paper in papers
            if keyword.lower()
            in paper["keywords"].lower()
        ]

    @classmethod
    def edit_paper(
            cls,
            paper_id,
            updated_paper
    ):

        papers = cls.get_all_papers()

        found = False

        for i, paper in enumerate(papers):

            if paper["paper_id"] == str(paper_id):

                papers[i] = updated_paper

                found = True

                break

        if not found:

            print("Paper ID not found.")

            return

        FileManager.write_csv(
            cls.PAPERS_FILE,
            cls.PAPER_FIELDS,
            papers
        )

        print(
            "Paper updated successfully."
        )

    @classmethod
    def delete_paper(
            cls,
            paper_id
    ):

        papers = cls.get_all_papers()

        updated = [

            paper

            for paper in papers

            if paper["paper_id"]
            != str(paper_id)

        ]

        FileManager.write_csv(
            cls.PAPERS_FILE,
            cls.PAPER_FIELDS,
            updated
        )

        print(
            "Paper deleted successfully."
        )