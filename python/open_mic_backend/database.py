import psycopg2

class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance


    def __init__(self, db_name, user, password, host, port):
        dsn = f"dbname={db_name} user={user} password={password} host={host} port={port}"
        if not hasattr(self, "connection"):  # initialize only once
            try:
                self.connection = psycopg2.connect(dsn)
                self.cursor = self.connection.cursor()
            except psycopg2.OperationalError as e:
                print("ERROR: Database connection could not be established! Error Message:")
                print(e)


    # Example: query("SELECT * FROM users WHERE id = %s", (1,))
    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.cursor.fetchall()


    # Example: execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Alice", "alice@example.com"))
    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        self.connection.commit()
