from movie import Movie
from user import User
from review import Review
from utils import clear_screen

from rich.prompt import Prompt


movie_manager = Movie()
user_manager = User()
review_manager = Review()

# Session to track logged-in user
session = {"user_id": None, "username": None, "is_admin": False}

def show_menu(if_logged, is_admin):
    print("\n===== IMDB-like App Menu =====")

    print("1. List Movies")
    print("2. Search Movies")
    print("3. Get Reviews for Movie")


    if ensure_logged_in():
        print("2. Logout User")
        print("4. Add Review")
        print("5. Like a Movie")

    else:
        print("2. Register/Login")
        

        print("--- You need to login for additional functionalities ---")

    if ensure_admin():
        print("4. Add Movie (Admin Only)")
        print("12. View Users (Admin Only)")
        print("6. Update Movie (Admin Only)")
        print("7. Delete Movie (Admin Only)")

    print("e Exit")

    print("==============================")

def ensure_logged_in():
    if session['user_id'] is None:
        print("You need to log in first!")
        return False
    return True

def ensure_admin():
    print(f"User ID: {session.get('user_id')}, Is Admin: {session.get('is_admin')}")
    if session['user_id'] is None:
        print("You need to log in first!")
        return False
    if not session['is_admin']:
        print("You need admin privileges to perform this action!")
        return False
    return True


def initialize_admin():
    if not user_manager.check_if_admin_exists():
        print("No admin user exists. Please create an admin account.")
        while True:
            username = input("Enter admin username: ").strip()
            password = input("Enter admin password: ").strip()
            if username and password:
                user_manager.register_user(username, password, is_admin=True)
                break
            else:
                print("Username and password cannot be empty. Please try again.")

def view_users():
    if ensure_logged_in() and ensure_admin():
        print("\n--- List of All Users ---")
        user_manager.get_all_users()
    else:
        print("Admin access required to view users.")




def main():

    clear_screen()
    
    # Ensure an admin account is created if it doesn't exist
    initialize_admin()
    first_run = True


    while True:
        if not first_run:
            print("--- Press enter to continue  ---")
            input()
            clear_screen()
        else:
            first_run = False
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            pass

        elif choice == "2":
            if session['user_id'] is not None:
                            print("\n--- Register User ---")
            while True:
                username = input("Enter username: ").strip()
                if not username:
                    print("Username cannot be empty. Please try again.")
                    continue
                password = input("Enter password: ").strip()
                if not password:
                    print("Password cannot be empty. Please try again.")
                    continue
                user_manager.register_user(username, password)
                break


                print(f"User '{session['username']}' is already logged in. Please log out first.")
                continue
            print("\n--- Login User ---")
            username = (Prompt.ask("Enter Username")).strip()
            
            password = input("Enter password: ").strip()
            if not username or not password:
                print("Username and password cannot be empty.")
                continue
            user = user_manager.login_user(username, password)
            if user:
                session['user_id'] = user[0]
                session['username'] = username
                session['is_admin'] = user[2]
                print(f"Logged in as {username}")
            else:
                print("Login failed. Please check your credentials.")

        elif choice == "3":
            if session['user_id'] is None:
                print("No user is currently logged in.")
            else:
                print(f"User '{session['username']}' logged out.")
                session['user_id'] = None
                session['username'] = None
                session['is_admin'] = False

        elif choice == "4":
            if ensure_logged_in() and ensure_admin():
                print("\n--- Add Movie ---")
                title = input("Enter movie title: ").strip()
                if not title:
                    print("Title cannot be empty.")
                    continue
                
                # Prompt for genre with validation
                print("Available genres:")
                print(", ".join(movie_manager.allowed_genres))
                genre = input("Enter movie genre: ").strip()
                if not genre:
                    print("Genre cannot be empty.")
                    continue

                release_date = input("Enter release date (YYYY-MM-DD): ").strip()
                if not release_date:
                    print("Release date cannot be empty.")
                    continue

                description = input("Enter description: ").strip()
                cast = input("Enter cast: ").strip()

                movie_manager.add_movie(title, genre, release_date, description, cast)

        elif choice == "5":
            print("\n--- List Movies ---")
            movie_manager.formatted_movie_list()  # Reuse the formatted movie list function

        elif choice == "6":
            if ensure_logged_in() and ensure_admin():
                print("\n--- Update Movie ---")
                movie_manager.formatted_movie_list()  # Display movies in a formatted manner before updating
                movie_id = input("Enter the Movie ID to update: ").strip()
                if not movie_id.isdigit():
                    print("Invalid movie ID. It must be a number.")
                    continue

                # Optionally, display current details for the selected movie
                movies = movie_manager.get_all_movie_details()
                for movie in movies:
                    if str(movie[0]) == movie_id:
                        print("\nCurrent Movie Details:")
                        print(f"Movie ID: {movie[0]}")
                        print(f"Title: {movie[1]}")
                        print(f"Genre: {movie[2]}")
                        print(f"Release Date: {movie[3]}")
                        print(f"Description: {movie[4]}")
                        print(f"Cast: {movie[5]}")
                        break
                else:
                    print(f"No movie found with Movie ID {movie_id}.")
                    continue

                # Prompt for new details (press Enter to keep current)
                title = input("Enter new title (or press Enter to keep current): ").strip()
                genre = input("Enter new genre (or press Enter to keep current): ").strip()
                if genre and genre not in movie_manager.allowed_genres:
                    print("Invalid genre. Update aborted.")
                    continue
                release_date = input("Enter new release date (YYYY-MM-DD) (or press Enter to keep current): ").strip()
                description = input("Enter new description (or press Enter to keep current): ").strip()
                cast = input("Enter new cast (or press Enter to keep current): ").strip()

                # If any field is left blank, pass None to keep current value
                title = title if title else None
                genre = genre if genre else None
                release_date = release_date if release_date else None
                description = description if description else None
                cast = cast if cast else None

                movie_manager.update_movie(movie_id, title, genre, release_date, description, cast)

        elif choice == "7":
            if ensure_logged_in() and ensure_admin():
                print("\n--- Delete Movie ---")
                movie_manager.formatted_movie_list()  # Display movies in a formatted manner before deleting
                movie_id = input("Enter the Movie ID to delete: ").strip()
                if not movie_id.isdigit():
                    print("Invalid Movie ID. It must be a number.")
                    continue

                # Confirm deletion
                confirm = input(f"Are you sure you want to delete Movie ID {movie_id}? (Y/N): ").strip().lower()
                if confirm == 'y':
                    movie_manager.delete_movie(movie_id)
                else:
                    print("Deletion cancelled.")

        elif choice == "8":
            if ensure_logged_in():
                print("\n--- Add Review ---")
                movie_manager.formatted_movie_list()  # Show movies in formatted manner before adding a review
                movie_id = input("Enter movie ID to review: ").strip()
                if not movie_id.isdigit():
                    print("Invalid Movie ID. It must be a number.")
                    continue
                review_text = input("Enter your review: ").strip()
                if not review_text:
                    print("Review text cannot be empty.")
                    continue
                try:
                    rating = float(input("Enter your rating (0.0 - 10.0): ").strip())
                    if rating < 0.0 or rating > 10.0:
                        print("Rating must be between 0.0 and 10.0.")
                        continue
                except ValueError:
                    print("Invalid rating. It must be a number between 0.0 and 10.0.")
                    continue
                review_manager.add_review(session['user_id'], movie_id, review_text, rating)

        elif choice == "9":
            print("\n--- Get Reviews for Movie ---")
            movie_manager.formatted_movie_list()  # Display movies before getting reviews
            movie_id = input("Enter the Movie ID to get reviews: ").strip()
            if not movie_id.isdigit():
                print("Invalid Movie ID. It must be a number.")
                continue
            review_manager.get_reviews_for_movie(movie_id)

        elif choice == "10":
            print("\n--- Search Movies ---")
            search_term = input("Enter search term (title/genre): ").strip()
            if not search_term:
                print("Search term cannot be empty.")
                continue
            movie_manager.search_movies(search_term)

        elif choice == "11":
            if ensure_logged_in():
                print("\n--- Like a Movie ---")
                movie_manager.formatted_movie_list()  # Reuse formatted list for liking a movie
                movie_id = input("Enter the Movie ID to like: ").strip()
                if not movie_id.isdigit():
                    print("Invalid Movie ID. It must be a number.")
                    return
                movie_manager.like_movie(movie_id)
        elif choice == "12":
            view_users()  # Call the function to display all users

        elif choice == "13":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()
