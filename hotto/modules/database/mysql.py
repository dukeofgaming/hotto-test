import mysql.connector
from flask import current_app

class MySQLDatabase:
    def __init__(self, config=None):
        # If no config is provided, use Flask app config
        if config is None:
            config = current_app.config['DB_CONFIG']
        self.config = config

    def connect(self):
        return mysql.connector.connect(**self.config)

    def fetch_all(self, query, params=None, dict_cursor=True):
        conn = self.connect()
        try:
            cursor = conn.cursor(dictionary=dict_cursor)
            cursor.execute(query, params or ())
            rows = cursor.fetchall()
            cursor.close()
            return rows
        finally:
            conn.close()
