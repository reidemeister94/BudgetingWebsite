import sqlite3
from sqlite3 import Error


def create_connection(db_file, schema_file="schema.sql"):
    """create a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        with open(schema_file) as fp:
            cur.executescript(fp.read())
        print("DB Correctly created")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    create_connection("database.db")
