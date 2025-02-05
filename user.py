from db import Database
import hashlib
from utils import print_table

class User:
    def __init__(self):
        self.db = Database()

    def register_user(self, username, password, is_admin=False):
        # Hash the password before storing it
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        query = """
        INSERT INTO users (username, password, is_admin) 
        VALUES (%s, %s, %s)
        """
        self.db.execute_query(query, (username, hashed_password, is_admin))
        
        if is_admin:
            print(f"Admin '{username}' created successfully!")
        else:
            print(f"User '{username}' registered successfully!")

    def login_user(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        query = "SELECT user_id, username, is_admin FROM users WHERE username=%s AND password=%s"
        user = self.db.fetch_query(query, (username, hashed_password))
        
        if user:
            print(f"Login successful! Welcome, {username}.")
            return user[0]  # Return user data: (user_id, username, is_admin)
        else:
            print("Invalid credentials.")
            return None

    def check_if_admin_exists(self):
        # Query the database to check if any admin exists
        query = "SELECT * FROM users WHERE is_admin = TRUE"
        admin = self.db.fetch_query(query)
        return len(admin) > 0

    def get_all_users(self):
        """ Retrieve and display all users in a formatted manner """
        query = "SELECT user_id, username, is_admin FROM users"
        users = self.db.fetch_query(query)
        
        if not users:
            print("No users available.")
            return
        columns = ["User ID", "Username", "is_Admin"]

        print_table("Users", columns, users)
