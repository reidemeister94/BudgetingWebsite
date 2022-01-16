import sqlite3
from typing import List
import pathlib
import os
from hashlib import sha256
import dateparser
import sys

curr_dir = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(curr_dir)
import db_queries


class DBHandler:
    def __init__(self, path_db="database.db") -> None:
        self.path_db = os.path.join(curr_dir, path_db)

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def get_db_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(
            self.path_db, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
        )
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

    ### RETRIEVE METHODS

    def get_user_info(self, cursor, username):
        if cursor is None:
            db_conn = self.get_db_connection()
            cursor = db_conn.cursor()
        result = cursor.execute(db_queries.get_user_info, [username]).fetchall()[0]
        return result

    def get_user_previsions(self, cursor, username):
        if cursor is None:
            db_conn = self.get_db_connection()
            cursor = db_conn.cursor()
        result = cursor.execute(db_queries.get_user_previsions, [username]).fetchall()
        return result

    def is_transaction_in_db(self, id_transaction, username):
        db_conn = self.get_db_connection()
        cursor = db_conn.cursor()
        result = cursor.execute(
            db_queries.check_transaction_in_db, [id_transaction, username]
        ).fetchall()
        if len(result) == 1:
            return True
        return False

    def get_user_categories(self, cursor, username):
        if cursor is None:
            db_conn = self.get_db_connection()
            cursor = db_conn.cursor()
        result = cursor.execute(db_queries.get_user_categories, [username]).fetchall()
        return result

    def get_user_history(self, username, start_date=None, end_date=None):
        db_conn = self.get_db_connection()
        cursor = db_conn.cursor()
        user_info = self.get_user_info(cursor, username)
        if start_date is not None and end_date is not None:
            start_date = dateparser.parse(start_date)
            end_date = dateparser.parse(end_date)
            user_transactions = db_queries.get_user_transactions_date_range
            args = [username, start_date, end_date]
        else:
            user_transactions = db_queries.get_user_transactions
            args = [username]
        user_transactions = cursor.execute(user_transactions, args).fetchall()
        user_categories = self.get_user_categories(cursor, username)
        user_previsions = self.get_user_previsions(cursor, username)
        db_conn.close()
        return {
            "user_info": user_info,
            "user_transactions": user_transactions,
            "user_categories": user_categories,
            "user_previsions": user_previsions,
        }

    ### INSERT METHODS
    def insert_user(self, username, password, starting_balance=None):
        try:
            password_digest = sha256(password.encode("utf-8")).hexdigest()
            row = [username, password_digest, starting_balance]
            db_conn = self.get_db_connection()
            cursor = db_conn.cursor()
            cursor.execute(db_queries.insert_user, row)
            db_conn.close()
            return True
        except:
            return False

    def insert_transaction(self, transaction_data):
        try:
            db_conn = self.get_db_connection()
            cursor = db_conn.cursor()
            cursor.execute(db_queries.insert_transaction, transaction_data)
            db_conn.commit()
            db_conn.close()
            return True
        except:
            return False

    def insert_category(self, category_data):
        try:
            db_conn = self.get_db_connection()
            cursor = db_conn.cursor()
            cursor.execute(db_queries.insert_category, category_data)
            db_conn.commit()
            db_conn.close()
            return True
        except:
            return False

    def insert_prevision(self, prevision_data):
        try:
            db_conn = self.get_db_connection()
            cursor = db_conn.cursor()
            cursor.execute(db_queries.insert_prevision, prevision_data)
            db_conn.commit()
            db_conn.close()
            return True
        except:
            return False

    ### UPDATE METHODS

    def update_transaction(self, transaction_data):
        try:
            db_conn = self.get_db_connection()
            cursor = db_conn.cursor()
            cursor.execute(db_queries.update_transaction, transaction_data)
            db_conn.commit()
            db_conn.close()
            return True
        except:
            return False

    def update_category(self, category_data):
        try:
            db_conn = self.get_db_connection()
            cursor = db_conn.cursor()
            cursor.execute(db_queries.update_category, category_data)
            db_conn.commit()
            db_conn.close()
            return True
        except:
            return False

    def update_prevision(self, prevision_data):
        try:
            db_conn = self.get_db_connection()
            cursor = db_conn.cursor()
            cursor.execute(db_queries.update_prevision, prevision_data)
            db_conn.commit()
            db_conn.close()
            return True
        except:
            return False

    ### DELETE METHODS

    def delete_transaction(self, transaction_data):
        try:
            db_conn = self.get_db_connection()
            cursor = db_conn.cursor()
            cursor.execute(db_queries.delete_transaction, transaction_data)
            db_conn.commit()
            db_conn.close()
            return True
        except:
            return False

    def delete_category(self, category_data):
        try:
            db_conn = self.get_db_connection()
            cursor = db_conn.cursor()
            cursor.execute(db_queries.delete_category, category_data)
            db_conn.commit()
            db_conn.close()
            return True
        except:
            return False

    def delete_prevision(self, prevision_data):
        try:
            db_conn = self.get_db_connection()
            cursor = db_conn.cursor()
            cursor.execute(db_queries.delete_prevision, prevision_data)
            db_conn.commit()
            db_conn.close()
            return True
        except:
            return False

    ### UTILS METHODS
    def category_transaction_is_present(self, category_transaction, username):
        db_conn = self.get_db_connection()
        cursor = db_conn.cursor()
        categories_user = self.get_user_categories(cursor, username)
        db_conn.commit()
        db_conn.close()
        for category in categories_user:
            if category_transaction == category["category_name"]:
                return True
        return False
