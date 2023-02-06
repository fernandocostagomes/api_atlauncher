import psycopg2

class PostgreSQL:
    def __init__(self, host, database, user, password):
        self.connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        self.cursor = self.connection.cursor()        

    def close(self):
        self.cursor.close()
        self.connection.close()

    def execute(self, sql, data=None):
        self.cursor.execute(sql, data)
        return self.cursor

    def commit(self):
        self.connection.commit()   