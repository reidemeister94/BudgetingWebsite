import sqlite3
from typing import List
import pathlib
import os

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
        # rows = cursor.execute("SELECT * FROM user").fetchall()
        print("ROWS")
        print(rows)
        print("=" * 75)
        return rows
