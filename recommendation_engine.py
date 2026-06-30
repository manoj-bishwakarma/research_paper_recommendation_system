class RecommendationEngine:

    @staticmethod
    def recommend(
            user_interest,
            papers
    ):

        recommendations = []

        interest = (
            user_interest.lower()
        )

        for paper in papers:

            category = (
                paper["category"]
                .lower()
            )

            keywords = (
                paper["keywords"]
                .lower()
            )

            if (
                interest in category
                or
                interest in keywords
            ):

                recommendations.append(
                    paper
                )

        return recommendations
