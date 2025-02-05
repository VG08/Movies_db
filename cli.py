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


def show_menu():
    print("\n===== The Movie Database =====")

    print("1. List Movies")
    print("2. Search Movies")
    print("3. Get Reviews for Movie")

    if is_logged_in():
        print("4. Get complete details for a Movie")
        print("5. Add Review")
        print("6. Like a Movie")

        print("u Logout User")

    else:
        print("u. Register/Login")

        print("\n --- You need to login for additional functionalities ---\n")

    if is_admin():


        print("==============================")
        print("7. View Users (Admin Only)")
        print("8. Add Movie (Admin Only)")
        print("9. Update Movie (Admin Only)")
        print("10. Delete Movie (Admin Only)")
    print("e Exit")

    print("==============================")


def is_logged_in():
    if session["user_id"] is None:
        return False
    return True


def is_admin():
    if not session["is_admin"]:
        return False
    return True


def ensure_logged_in():
    if is_logged_in():

        return True
    print("You need to log in first!")
    return False


def ensure_admin():
    
    if not is_logged_in:
        print("You need to log in first!")
        return False
    if is_admin:
        return True
    print("You need admin privileges to perform this action!")
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
            print("\n--- List Movies ---")
            movie_manager.formatted_movie_list()  # Reuse the formatted movie list function

        elif choice == "u":
            if session["user_id"] is not None:
                print(f"User '{session['username']}' logged out.")
                session["user_id"] = None
                session["username"] = None
                session["is_admin"] = False

            else:

                ans = Prompt.ask("New User(n) or Existing(l)?", choices=["n", "l"])
                if ans == "l":
                    print("\n--- Login User ---")

                    username = input("Enter username: ").strip()

                    password = input("Enter password: ").strip()
                    if not username or not password:
                        print("Username and password cannot be empty.")
                        continue
                    user = user_manager.login_user(username, password)
                    if user:
                        session["user_id"] = user[0]
                        session["username"] = username
                        session["is_admin"] = user[2]
                        print(f"Logged in as {username}")
                    else:
                        print("Login failed. Please check your credentials.")
                elif ans == "n":
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

                        print("You will need to login to continue")
                        break

        elif choice == "2":
            print("\n--- Search Movies ---")
            search_term = input("Enter search term (title/genre): ").strip()
            if not search_term:
                print("Search term cannot be empty.")
                continue
            movie_manager.search_movies(search_term)
        elif choice == "3":
            print("\n--- Get Reviews for Movie ---")
            search_term = input("Search for the movie you want reviews for (title/genre): ").strip()
            if not search_term:
                print("Search term cannot be empty.")
                continue
            if not movie_manager.search_movies(search_term):
                continue
    
            movie_id = input("Enter the Movie ID for which you want reviews: ").strip()
            if not movie_id.isdigit():
                print("Invalid Movie ID. It must be a number.")
                continue
            review_manager.get_reviews_for_movie(movie_id)
        elif choice == "4":
            print("\n--- Get Reviews for Movie ---")
            search_term = input("Search for the movie you want reviews for (title/genre): ").strip()
            if not search_term:
                print("Search term cannot be empty.")
                continue
            if not movie_manager.search_movies(search_term):
                continue
            

            movie_id = input("Enter the Movie ID to see: ").strip()
            
            if not movie_id.isdigit():
                print("Invalid movie ID. It must be a number.")
                continue

            movies = movie_manager.get_all_movies_details()
            clear_screen()
            print("\n--- Movie Details---")

            for movie in movies:
                if str(movie[0]) == movie_id:
                    print("\nCurrent Movie Details:")
                    print(f"Movie ID: {movie[0]}")
                    print(f"Title: {movie[1]}")
                    print(f"Genre: {movie[2]}")
                    print(f"Release Date: {movie[3]}")
                    print(f"Description: {movie[4]}")
                    print(f"Cast: {movie[5]}")
                    print()
                    break
            else:
                print(f"No movie found with Movie ID {movie_id}.")
                continue

        elif choice == "5":
            if ensure_logged_in():
                print("\n--- Add Review ---")
                
                search_term = input("Search for the movie you want to review(title/genre): ").strip()
                if not search_term:
                    print("Search term cannot be empty.")
                    continue
                if not movie_manager.search_movies(search_term):
                    continue
                print()
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
                
                review_manager.add_review(
                    session["user_id"], movie_id, review_text, rating
                )
                movie_manager.update_rating(movie_id)

        elif choice == "6":
            if ensure_logged_in():
                print("\n--- Like a Movie ---")
                search_term = input("Search for the movie you want to like (title/genre): ").strip()
                if not search_term:
                    print("Search term cannot be empty.")
                    continue
                if not movie_manager.search_movies(search_term):
                    continue
                movie_id = input("Enter the Movie ID to like: ").strip()
                if not movie_id.isdigit():
                    print("Invalid Movie ID. It must be a number.")
                    return
                movie_manager.like_movie(movie_id)
        elif choice == "7":
            view_users()  # Call the function to display all users

        elif choice == "8":
            if ensure_logged_in() and ensure_admin():
                print("\n--- Add Movie ---")
                title = input("Enter movie title: ").strip()
                if not title:
                    print("Title cannot be empty.")
                    continue

                # Prompt for genre with validation
                print("Available genres:")
                print(", ".join(movie_manager.allowed_genres))
                genre = Prompt.ask("Enter movie genre: ", choices=movie_manager.allowed_genres).strip()

                release_date = input("Enter release date (YYYY-MM-DD): ").strip()
                if not release_date:
                    print("Release date cannot be empty.")
                    continue

                description = input("Enter description: ").strip()
                cast = input("Enter cast: ").strip()

                movie_manager.add_movie(title, genre, release_date, description, cast)

        elif choice == "9":
            if ensure_logged_in() and ensure_admin():
                print("\n--- Update Movie ---")
                movie_manager.formatted_movie_list()  # Display movies in a formatted manner before updating
                movie_id = input("Enter the Movie ID to update: ").strip()
                if not movie_id.isdigit():
                    print("Invalid movie ID. It must be a number.")
                    continue

                movies = movie_manager.get_all_movies_details()
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
                title = input(
                    "Enter new title (or press Enter to keep current): "
                ).strip()
                genre = Prompt.ask(
                    "Enter new genre (or press Enter to keep current): ",
                    choices=movie_manager.allowed_genres +[""]
                ).strip()

                release_date = input(
                    "Enter new release date (YYYY-MM-DD) (or press Enter to keep current): "
                ).strip()
                description = input(
                    "Enter new description (or press Enter to keep current): "
                ).strip()
                cast = input(
                    "Enter new cast (or press Enter to keep current): "
                ).strip()


                movie_manager.update_movie(
                    movie_id=movie_id, title=title, genre=genre,release_date= release_date, description=description, cast=cast
                )

        elif choice == "10":
            if ensure_logged_in() and ensure_admin():
                print("\n--- Delete Movie ---")
                movie_manager.formatted_movie_list()  # Display movies in a formatted manner before deleting
                movie_id = input("Enter the Movie ID to delete: ").strip()
                if not movie_id.isdigit():
                    print("Invalid Movie ID. It must be a number.")
                    continue

                # Confirm deletion
                confirm = (
                    Prompt.ask(
                        f"Are you sure you want to delete Movie ID {movie_id}?",
                        choices=["y","n"]
                    )
                    .strip()
                    .lower()
                )
                if confirm == "y":
                    #Delete Reviews first
                    review_manager.delete_reviews_for_movie(movie_id=movie_id)

                    movie_manager.delete_movie(movie_id)
                else:
                    print("Deletion cancelled.")

        elif choice == "e":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option from the menu.")


if __name__ == "__main__":
    main()
