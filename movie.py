from db import Database
from datetime import datetime
from utils import print_table
class Movie:
    def __init__(self):
        self.db = Database()
        # List of allowed genres
        self.allowed_genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Romance', 'Documentary', 'Fantasy', 'Adventure']

    def validate_genre(self, genre):
        """ Validate if the genre is from the allowed list """
        if genre in self.allowed_genres:
            return True
        else:
            print(f"Invalid genre. Allowed genres are: {', '.join(self.allowed_genres)}")
            return False
    


    def like_movie(self, movie_id):
        """ Increment the like count of a movie """
        # Check if the movie exists
        query_check = "SELECT * FROM movies WHERE movie_id = %s"
        movie = self.db.fetch_query(query_check, (movie_id,))
        if not movie:
            print(f"No movie found with Movie ID {movie_id}.")
            return
        # Increment the like count
        try:
            query_update = "UPDATE movies SET likes = likes + 1 WHERE movie_id = %s"
            self.db.execute_query(query_update, (movie_id,))
            print(f"Movie ID {movie_id} liked successfully!")
        except Exception as e:
            print(f"Error liking movie: {e}")

    def validate_date(self, date_str):
        """ Validate if the date is in the correct format YYYY-MM-DD and is a valid date """
        try:
            # Convert the string into a date to ensure it is valid
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            print("Invalid date format or invalid date value. Please enter the date in YYYY-MM-DD format.")
            return False

    def add_movie(self, title, genre, release_date, description, cast):
        """ Add a movie to the database with proper validation """
        # Check if genre is valid
        if not self.validate_genre(genre):
            print("Movie not added successfully due to invalid genre.")
            return
        
        # Check if release date is valid
        if not self.validate_date(release_date):
            print("Movie not added successfully due to invalid release date.")
            return

        try:
            query = """
            INSERT INTO movies (title, genre, release_date, description, cast) 
            VALUES (%s, %s, %s, %s, %s)
            """
            r = self.db.execute_query(query, (title, genre, release_date, description, cast))
            if not r:
                raise Exception()
            print(f"Movie '{title}' added successfully!")
        except Exception as e:
            print(f"Error adding movie: {e}")
            print("Movie not added successfully due to an error.")


    def get_all_movies_details(self):
        """ Fetch all movie details from the database """
        query = "SELECT * FROM movies"
        movies = self.db.fetch_query(query)
        return movies
    
    def get_movie_details(self, movie_id):
        """ Fetch all details of a movie from the database"""    
        query_check = "SELECT * FROM movies WHERE movie_id=%s"
        movie = self.db.fetch_query(query_check, (movie_id,)) 
        if movie:
            return movie[0]
        else: 
            return False
    def update_movie(self, movie_id, title=None, genre=None, release_date=None, description=None, cast=None, rating=None):
        """ Update a movie's details """
        # Validate inputs if they are provided
        if genre and not self.validate_genre(genre):
            print("Movie not updated successfully due to invalid genre.")
            return
        if release_date and not self.validate_date(release_date):
            print("Movie not updated successfully due to invalid release date.")
            return

        movie = self.get_movie_details(movie_id=movie_id)
        title = title if title else movie[1]
        genre = genre if genre else movie[2]
        release_date = release_date if release_date else movie[3]
        description = description if description else movie[4]
        cast = cast if cast else movie[5]
       



        try:
            query = "UPDATE movies SET title=%s, genre=%s, release_date=%s, description=%s, cast=%s WHERE movie_id=%s"
            self.db.execute_query(query, (title, genre, release_date, description, cast, movie_id))
            print(f"Movie ID {movie_id} updated successfully!")
        except Exception as e:
            print(f"Error updating movie: {e}")
            print("Movie not updated successfully due to an error.")

    def delete_movie(self, movie_id):
        """ Delete a movie from the database """
        # First, check if the movie exists
        movie = self.get_movie_details(movie_id=movie_id)
        if not movie:
            print(f"No movie found with Movie ID {movie_id}.")
            return
        
        try:
            query = "DELETE FROM movies WHERE movie_id=%s"
            self.db.execute_query(query, (movie_id,))
            print(f"Movie ID {movie_id} deleted successfully!")
        except Exception as e:
            print(f"Error deleting movie: {e}")
            print("Movie not deleted successfully due to an error.")

    def search_movies(self, search_term):
        """ Search for movies by title or genre """
        query = """
        SELECT movie_id, title, genre, description, rating, likes FROM movies WHERE title LIKE %s OR genre LIKE %s
        """
        search_term = f"%{search_term}%"
        
        movies = self.db.fetch_query(query, (search_term, search_term))
        if movies:
            columns = ["Movie ID", "Title", "Genre", "Description", "Rating", "Likes"]

            print_table("Movies", columns, movies)
            return True

        else:
            print("No movies found.")
            return False

    def update_rating(self, movie_id):
        query = "SELECT COUNT(*) FROM reviews where movie_id=%s"
        n = self.db.fetch_query(query, (movie_id,))
        n = n[0][0]
        query = "select sum(rating) from reviews where movie_id=%s"
        s_rating = self.db.fetch_query(query, (movie_id,))[0][0]
        
        new_rating = s_rating/n
        query = "update movies set rating=%s where movie_id=%s"
        self.db.execute_query(query, (new_rating, movie_id))

    def formatted_movie_list(self):
        """ Display all movies in a formatted manner """
        query = """
        SELECT movie_id, title, genre, description, rating, likes FROM movies"""
        movies = self.db.fetch_query(query)
        if not movies:
            print("No movies available.")
            return
        columns = ["Movie ID", "Title",  "Genre", "Description", "Rating", "Likes"]
        print_table("Movies", columns, movies)

