"""
Amazon Object Oriented Design Question

Designing an API to fetch all reviews and comments,
with an Object-Oriented Design (OOD) approach,
involves defining clear data structures and interactions.
"""

from datetime import datetime
from typing import List, Optional


# Core Entities
class Comment:
    def __init__(self, comment_id: int, review_id: int, user_id: int,
                 content: str, language: str, timestamp: Optional[datetime] = None):
        self.comment_id = comment_id
        self.review_id = review_id
        self.user_id = user_id
        self.content = content
        self.language = language
        self.timestamp = timestamp or datetime.utcnow()

    def __repr__(self):
        return f"Comment(id={self.comment_id}, lang={self.language}, content='{self.content}')"


class Review:
    def __init__(self, review_id: int, user_id: int, product_id: int,
                 content: str, language: str, rating: float,
                 timestamp: Optional[datetime] = None):
        self.review_id = review_id
        self.user_id = user_id
        self.product_id = product_id
        self.content = content
        self.language = language
        self.rating = rating
        self.timestamp = timestamp or datetime.utcnow()
        self.comments: List[Comment] = []

    def add_comment(self, comment: Comment):
        self.comments.append(comment)

    def __repr__(self):
        return f"Review(id={self.review_id}, lang={self.language}, rating={self.rating})"


# ReviewsDB (simulates DB)
class ReviewRepository:
    def __init__(self):
        self.reviews: List[Review] = []

    def add_review(self, review: Review):
        self.reviews.append(review)

    def fetch_all(self, product_id: Optional[int] = None) -> List[Review]:
        if product_id is None:
            return self.reviews
        return [r for r in self.reviews if r.product_id == product_id]

    def get(self, review_id: int) -> Optional[Review]:
        for r in self.reviews:
            if r.review_id == review_id:
                return r
        return None


# API Service Layer
class ReviewService:
    def __init__(self, review_repo: ReviewRepository):
        self.review_repo = review_repo

    def get_reviews(self, product_id: Optional[int] = None, language: Optional[str] = None) -> List[Review]:
        reviews = self.review_repo.fetch_all(product_id=product_id)
        if language:
            reviews = [r for r in reviews if r.language == language]
        return reviews

    def get_comments_for_review(self, review_id: int, language: Optional[str] = None) -> List[Comment]:
        review = self.review_repo.get(review_id)
        if not review:
            return []
        comments = review.comments
        if language:
            comments = [c for c in comments if c.language == language]
        return comments

    def get_reviews_with_comments(self, product_id: Optional[int] = None, language: Optional[str] = None):
        reviews = self.get_reviews(product_id, language)
        result = []
        for r in reviews:
            filtered_comments = r.comments
            if language:
                filtered_comments = [c for c in r.comments if c.language == language]
            result.append({
                "review": r,
                "comments": filtered_comments
            })
        return result


if __name__ == "__main__":
    repo = ReviewRepository()

    # Create reviews
    review1 = Review(1, user_id=101, product_id=1001, content="Great product!", language="en", rating=4.5)
    review2 = Review(2, user_id=102, product_id=1001, content="Muy bueno!", language="es", rating=5.0)

    # Add comments
    review1.add_comment(Comment(1, review_id=1, user_id=201, content="I agree!", language="en"))
    review1.add_comment(Comment(2, review_id=1, user_id=202, content="Me encanta!", language="es"))
    review2.add_comment(Comment(3, review_id=2, user_id=203, content="Excelente!", language="es"))

    # Add reviews to repository
    repo.add_review(review1)
    repo.add_review(review2)

    service = ReviewService(repo)

    # Fetch all reviews with their comments
    all_reviews_and_comments = service.get_reviews_with_comments()

    # Example: Fetch only English reviews and comments
    english_reviews_and_comments = service.get_reviews_with_comments(language="en")
    for item in english_reviews_and_comments:
        print("English Review:", item["review"])
        print("English Comments:", item["comments"])
        print("------")

