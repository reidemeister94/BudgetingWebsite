import sqlite3
from typing import List
import pathlib
import os
from hashlib import sha256

curr_dir = str(pathlib.Path(__file__).parent.resolve())


class DBHandler:
    def __init__(self, path_db="database.db") -> None:
        self.path_db = os.path.join(curr_dir, path_db)

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def get_db_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.path_db)
        conn.row_factory = self.dict_factory
        return conn

    def get_all_elements_from_table(
        self, connection: sqlite3.Connection, table_name: str
    ) -> List:
        cursor = connection.cursor()
        rows = cursor.execute(f"SELECT * FROM {table_name}").fetchall()
        connection.close()
        # rows = cursor.execute("SELECT * FROM user").fetchall()
        # print("ROWS")
        # print(rows)
        # print("=" * 75)
        return rows

    def check_user_exists(self, username):
        db_conn = self.get_db_connection()
        users = self.get_all_elements_from_table(db_conn, "user")
        db_conn.close()
        for user in users:
            # print(user["username"], user["password"], password_digest)
            if user["username"] == username:
                return True
        return False

    def check_credentials(self, username, password):
        db_conn = self.get_db_connection()
        users = self.get_all_elements_from_table(db_conn, "user")
        db_conn.close()
        password_digest = sha256(password.encode("utf-8")).hexdigest()
        for user in users:
            # print(user["username"], user["password"], password_digest)
            if user["password"] == password_digest and user["username"] == username:
                return True
        return False

    def insert_row_to_table(self, conn, table, row):
        cols = ", ".join('"{}"'.format(col) for col in row.keys())
        vals = ", ".join(":{}".format(col) for col in row.keys())
        sql = 'INSERT INTO "{0}" ({1}) VALUES ({2})'.format(table, cols, vals)
        conn.cursor().execute(sql, row)
        conn.commit()

    def add_user_to_db(self, username, password):
        db_conn = self.get_db_connection()
        password_digest = sha256(password.encode("utf-8")).hexdigest()
        row = {"username": username, "password": password_digest}
        self.insert_row_to_table(db_conn, "user", row)
        db_conn.close()
