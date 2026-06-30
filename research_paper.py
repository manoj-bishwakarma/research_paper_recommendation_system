class ResearchPaper:
    def __init__(self, paper_id, title, author, category, keywords, abstract="", link=""):
        self.paper_id = paper_id
        self.title = title
        self.author = author
        self.category = category
        self.keywords = keywords
        self.abstract = abstract
        self.link = link

    def display(self):
        print(f"ID: {self.paper_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Category: {self.category}")
        print(f"Keywords: {self.keywords}")
        print(f"Abstract: {self.abstract}")
        print(f"Link: {self.link}")