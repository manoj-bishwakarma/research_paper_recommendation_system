from user import User

class Admin(User):
    def __init__(self, user_id, username, password):
        super().__init__(user_id, username, password, "Administrator")

    def add_paper(self):
        print("Add Paper operation")

    def edit_paper(self):
        print("Edit Paper operation")

    def delete_paper(self):
        print("Delete Paper operation")

    def view_all_papers(self):
        print("View All Papers operation")