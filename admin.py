from user import User
from train_model import train_model as train_recommendation_model


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

    def retrain_model(self):
        """
        Retrain the recommendation model on the current papers.csv
        and overwrite model.pkl / vectorizer.pkl.
        """
        print("\nRetraining recommendation model, please wait...")

        train_recommendation_model()

        print("Recommendation model retrained successfully.")
