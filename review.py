from db import Database

class Review:
    def __init__(self):
        self.db = Database()

    def add_review(self, user_id, movie_id, review_text, rating):
        query = """
        INSERT INTO reviews (user_id, movie_id, review_text, rating) 
        VALUES (%s, %s, %s, %s)
        """
        self.db.execute_query(query, (user_id, movie_id, review_text, rating))
        print("Review added successfully!")

    def get_reviews_for_movie(self, movie_id):
        query = "SELECT review_text, rating FROM reviews WHERE movie_id=%s"
        reviews = self.db.fetch_query(query, (movie_id,))
        for review in reviews:
            print(f"Rating: {review[1]} - {review[0]}")
