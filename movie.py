from db import Database
from datetime import datetime
from rich.table import Table
from  rich.console import Console
from utils import print_table
class Movie:
    def __init__(self):
        self.db = Database()
        # List of allowed genres
        self.allowed_genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Romance', 'Documentary']

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
            self.db.execute_query(query, (title, genre, release_date, description, cast))
            print(f"Movie '{title}' added successfully!")
        except Exception as e:
            print(f"Error adding movie: {e}")
            print("Movie not added successfully due to an error.")
    
    #old redundant function
    # def list_movies(self):
    #     """ List all movies from the database """
    #     query = "SELECT * FROM movies"
    #     movies = self.db.fetch_query(query)
    #     if movies:
            
    #         for movie in movies:
    #             print(f"{movie[0]} - {movie[1]} ({movie[2]})")
    #     else:
    #         print("No movies found.")

    def get_all_movie_details(self):
        """ Fetch all movie details from the database """
        query = "SELECT * FROM movies"
        movies = self.db.fetch_query(query)
        return movies

    def update_movie(self, movie_id, title=None, genre=None, release_date=None, description=None, cast=None):
        """ Update a movie's details """
        # Validate inputs if they are provided
        if genre and not self.validate_genre(genre):
            print("Movie not updated successfully due to invalid genre.")
            return
        if release_date and not self.validate_date(release_date):
            print("Movie not updated successfully due to invalid release date.")
            return

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
        query_check = "SELECT * FROM movies WHERE movie_id=%s"
        movie = self.db.fetch_query(query_check, (movie_id,))
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
        SELECT * FROM movies WHERE title LIKE %s OR genre LIKE %s
        """
        search_term = f"%{search_term}%"
        movies = self.db.fetch_query(query, (search_term, search_term))
        if movies:
            columns = ["Movie ID", "Title", "Genre", "Release Date", "Description", "Cast", "Rating", "Likes"]
            print_table("Movies", columns, movies)
        else:
            print("No movies found.")

    def formatted_movie_list(self):
        """ Display all movies in a formatted manner """
        movies = self.get_all_movie_details()
        if not movies:
            print("No movies available.")
            return
        columns = ["Movie ID", "Title",  "Genre", "Release Date", "Description", "Cast", "Rating", "Likes"]
        print_table("Movies", columns, movies)

