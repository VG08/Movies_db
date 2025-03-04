import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        try:
            # Establish the database connection
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",  
                password="mysql",  
                database="imdb_db"  
            )
            if self.connection.is_connected():
                print("Successfully connected to the database")
            self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Error while connecting to the database: {e}")
            self.connection = None

    def execute_query(self, query, params=None):
        try:
            if self.connection.is_connected():
                self.cursor.execute(query, params)
                self.connection.commit()
                return True
        except Error as e:
            print(f"Error executing query: {e}")
            return False

    def fetch_query(self, query, params=None):
        try:
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()

                self.cursor.execute(query, params)
                result = self.cursor.fetchall()
                return result
        except Error as e:
            print(f"Error fetching data: {e}")
            return None

    def close(self):
        try:
            if self.connection.is_connected():
                self.cursor.close()
                self.connection.close()
                print("Connection closed successfully")
        except Error as e:
            print(f"Error closing the connection: {e}")
