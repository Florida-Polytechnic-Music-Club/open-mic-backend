from .database import Database

class DatabaseHandler():

    def __init__(self):
        # Create database connection
        db_name = "users"
        db_user = "admin"
        db_password = "password"
        db_host = "localhost"
        db_port = "5432"
        # Attempt Database connection
        self.database = Database(db_name, db_user, db_password, db_host, db_port)        


    def send_query(self, sql):
        # Do SQL santizition here
        clean_query = sql

        return self.database.query(clean_query)
        
    def send_execute(self, sql):
        # Do SQL santizition here
        clean_query = sql
        self.database.execute(clean_query)




