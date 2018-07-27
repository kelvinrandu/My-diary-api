from psycopg2 import connect, extras

class DatabaseConnect():
    """Initializes connection to the database and executes queries"""
    def __init__(self):
        self.conn = connect("dbname=mydiary user=randu password=1234 host=localhost")
        self.cursor = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        self.conn.autocommit = True
