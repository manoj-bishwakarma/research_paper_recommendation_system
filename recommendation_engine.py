import os
import joblib
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity

from history_manager import HistoryManager


class RecommendationEngine:

    BASE_DIR = os.path.dirname(
        os.path.abspath(__file__)
    )

    MODEL_PATH = os.path.join(
        BASE_DIR,
        "model",
        "model.pkl"
    )

    VECTORIZER_PATH = os.path.join(
        BASE_DIR,
        "model",
        "vectorizer.pkl"
    )

    PAPERS_PATH = os.path.join(
        BASE_DIR,
        "data",
        "papers.csv"
    )

    model = joblib.load(MODEL_PATH)

    vectorizer = joblib.load(VECTORIZER_PATH)

    papers = pd.read_csv(PAPERS_PATH)

    # Pre-compute each paper's TF-IDF vector once, using the same
    # text fields the model itself was trained on
    papers["text"] = (
        papers["title"].fillna("")
        + " "
        + papers["keywords"].fillna("")
        + " "
        + papers["abstract"].fillna("")
    )

    paper_vectors = vectorizer.transform(papers["text"])

    # Populated on each call to recommend(); used for the empty-state message
    last_attempted_categories = []
    last_predicted_category = None

    @classmethod
    def reload_model(cls):
        """
        Reload model.pkl, vectorizer.pkl, and papers.csv from disk.
        Call this after retraining so the running app picks up the
        new model without needing a restart.
        """

        cls.model = joblib.load(cls.MODEL_PATH)

        cls.vectorizer = joblib.load(cls.VECTORIZER_PATH)

        cls.papers = pd.read_csv(cls.PAPERS_PATH)

        cls.papers["text"] = (
            cls.papers["title"].fillna("")
            + " "
            + cls.papers["keywords"].fillna("")
            + " "
            + cls.papers["abstract"].fillna("")
        )

        cls.paper_vectors = cls.vectorizer.transform(cls.papers["text"])

    @classmethod
    def recommend(
            cls,
            user
    ):

        # -----------------------------
        # Create user profile
        # -----------------------------

        profile = user["interest"]

        history = HistoryManager.get_user_history(
            user["user_id"]
        )

        for record in history:

            profile += " " + record["title"]

        profile_vector = cls.vectorizer.transform(
            [profile]
        )

        # If none of the profile's words exist in the trained vocabulary,
        # the vector is all zeros and cosine similarity will be 0% for
        # every paper. Flag this so we can fall back to keyword matching.
        profile_is_empty = profile_vector.nnz == 0

        # -----------------------------
        # Predict category (ranked by confidence)
        # -----------------------------

        proba = cls.model.predict_proba(profile_vector)[0]

        classes = cls.model.classes_

        ranked_indices = proba.argsort()[::-1]

        # -----------------------------
        # Per-paper similarity to the user's profile
        # (this is what makes scores differ paper-to-paper)
        # -----------------------------

        similarities = cosine_similarity(
            profile_vector,
            cls.paper_vectors
        )[0]

        # -----------------------------
        # Already read papers
        # -----------------------------

        read_ids = set()

        for record in history:

            read_ids.add(
                str(record["paper_id"])
            )

        profile_words = set(profile.lower().split())

        cls.last_attempted_categories = []

        for cat_index in ranked_indices:

            category = classes[cat_index]
            confidence = proba[cat_index] * 100

            cls.last_attempted_categories.append(
                (category, confidence)
            )

            recommendations = []

            for row_index, paper in cls.papers.iterrows():

                if (
                    paper["category"].strip().lower()
                    != category.strip().lower()
                ):
                    continue

                if str(paper["paper_id"]) in read_ids:
                    continue

                paper_dict = paper.to_dict()

                keywords = [
                    k.strip().lower()
                    for k in str(paper["keywords"]).split(",")
                    if k.strip()
                ]

                profile_lower = profile.lower()

                # Substring matching instead of exact whole-word matching --
                # so "cnn" matches "convolutional neural network" mentions,
                # and multi-word keywords like "graph neural network" match
                # even if the user only typed "graph learning".
                matched = [
                    k for k in keywords
                    if k in profile_lower
                    or any(
                        word in profile_words
                        for word in k.split()
                    )
                ]

                reasons = [
                    f"Matches your predicted interest category: {category}"
                ]

                if profile_is_empty:

                    # No TF-IDF overlap possible; score using how many
                    # of the paper's own keywords appear literally in
                    # the raw profile text instead.
                    if keywords:
                        similarity_score = (
                            len(matched) / len(keywords)
                        ) * 100
                    else:
                        similarity_score = 0

                    if matched:
                        reasons.append(
                            f"Shares keywords with your interests: {', '.join(matched)}"
                        )
                    else:
                        reasons.append(
                            "No direct keyword overlap found; ranked by category only."
                        )

                else:

                    # Score = how similar THIS paper is to the profile,
                    # scaled to a 0-100% range
                    similarity_score = similarities[row_index] * 100

                    if matched:
                        reasons.append(
                            f"Shares keywords with your interests: {', '.join(matched)}"
                        )

                paper_dict["score"] = similarity_score
                paper_dict["reason"] = reasons

                recommendations.append(paper_dict)

            if recommendations:

                recommendations.sort(
                    key=lambda p: p["score"],
                    reverse=True
                )

                # Rescale scores within this batch so the strongest match
                # displays near 100% and weaker ones scale proportionally
                # beneath it. This is cosmetic only -- it does not change
                # the ranking, only how the percentage reads.
                top_score = recommendations[0]["score"]

                if top_score > 0:

                    for paper_dict in recommendations:

                        paper_dict["score"] = (
                            paper_dict["score"] / top_score
                        ) * 100

                cls.last_predicted_category = category

                return recommendations

        # -----------------------------
        # Nothing found in any category
        # -----------------------------

        cls.last_predicted_category = classes[ranked_indices[0]]

        return []
