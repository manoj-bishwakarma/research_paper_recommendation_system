class User:
    def __init__(self, user_id, username, password, interest):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.interest = interest
        self.favorites = []
        self.history = []

    def add_favorite(self, paper_id):
        if paper_id not in self.favorites:
            self.favorites.append(paper_id)

    def add_history(self, paper_id):
        self.history.append(paper_id)

    def update_interest(self, new_interest):
        self.interest = new_interest

    def display_profile(self):
        print("----- USER PROFILE -----")
        print(f"ID: {self.user_id}")
        print(f"Username: {self.username}")
        print(f"Interest: {self.interest}")