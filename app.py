import os
import datetime
from flask import (
    Flask,
    json,
    jsonify,
    request,
    session,
    render_template_string,
    redirect,
    url_for,
)
from pprint import pprint
from string import printable
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import uuid
from db.db_handler import DBHandler

# configuration
DEBUG = True


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = os.environ["finance_app_secret_key"]
jwt = JWTManager(app)
# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

db_handler = DBHandler()


# @app.route("/", methods=["GET"])
# def home():
#     response_object = {"status": "success"}
#     db_conn = db_handler.get_db_connection()
#     users = db_handler.get_all_elements_from_table(db_conn, "user")
#     response_object["users"] = users
#     return jsonify(response_object)


def get_user_history(username, start_date, end_date):
    return db_handler.get_user_history(username, start_date, end_date)


def date_formatted_correctly(date_string):
    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except:
        return False


def clean_description(description):
    description = description.decode("utf-8", "ignore").encode("utf-8")
    return "".join(char for char in description if char in printable)


def amount_formatted_correctly(amount):
    try:
        amount = float(amount)
        if amount >= 0:
            return True
        else:
            return False
    except ValueError:
        return False


def transaction_type_formatted_correctly(transaction_type):
    try:
        transaction_type = int(transaction_type)
        if transaction_type == 0 or transaction_type == 1:
            return True
        else:
            return False
    except Exception as e:
        return False


def dashboard_body_correct(start_date, end_date):
    if (
        (start_date is not None and end_date is None)
        or (start_date is None and end_date is not None)
    ) or (
        (start_date is not None and end_date is not None)
        and (
            (type(start_date) != str or type(start_date) != str)
            or (
                not date_formatted_correctly(start_date)
                or not date_formatted_correctly(end_date)
            )
        )
    ):
        return False
    return True


def is_transaction_payload_healthy(request_json, username_jwt):
    keys = [
        "account_name",
        "transaction_date",
        "amount",
        "category",
        "transaction_type",
        "transaction_description",
    ]
    if any([key not in request_json for key in keys]):
        return False
    if username_jwt != request_json["account_name"]:
        return False
    if not date_formatted_correctly(request_json["transaction_date"]):
        return False
    if not amount_formatted_correctly(request_json["amount"]):
        return False
    if not db_handler.category_transaction_is_present(
        request_json["category"], username_jwt
    ):
        return False
    if not transaction_type_formatted_correctly(request_json["transaction_type"]):
        return False
    # account_name,transaction_date,amount,category,transaction_type,transaction_description
    return True


@app.route("/transaction/<id>", methods=["POST", "PUT", "DELETE"])
@jwt_required()
def process_transaction(id):
    username_jwt = get_jwt_identity()
    if request.method == "POST":
        payload_is_healthy = is_transaction_payload_healthy(request.json, username_jwt)
        if payload_is_healthy:
            success = db_handler.insert_transaction(
                [
                    request.json["account_name"],
                    request.json["transaction_date"],
                    request.json["amount"],
                    request.json["category"],
                    request.json["transaction_type"],
                    request.json["transaction_description"],
                ]
            )
            if success:
                return jsonify({"msg": "ok"})
            else:
                return jsonify({"msg": "KO"}), 500
        return jsonify({"msg": "bad request"}), 400


@app.route("/dashboard", methods=["POST"])
@jwt_required()
def dashboard():
    username = get_jwt_identity()
    if username:
        # print(f"IDENTITY USER: {username}")
        if request.json is None:
            return jsonify({"user_history": db_handler.get_user_history(username)})
        start_date = request.json.get("start_date", None)
        end_date = request.json.get("end_date", None)
        # print(start_date, end_date)
        if not dashboard_body_correct(start_date, end_date):
            return jsonify({"msg": "bad format"}), 400
        try:
            user_history = get_user_history(username, start_date, end_date)
            return jsonify(user_history)
        except Exception as e:
            print(str(e))
            return jsonify({"msg": "something went wrong"}), 400
    else:
        return jsonify({"msg": "not authorized"}), 401


# @app.route("/", methods=["GET"])
# @jwt_required(optional=True)
# def optionally_protected():
#     current_identity = get_jwt_identity()
#     if current_identity:
#         return jsonify({"msg": "logged"})
#     else:
#         return jsonify({"msg": "not logged"})


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user_exists = db_handler.check_credentials(username, password)
    if not user_exists:
        return jsonify({"msg": "bad username or password"}), 401
    # additional_claims = {"username": username}
    # access_token = create_access_token(username, additional_claims=additional_claims)
    access_token = create_access_token(
        username, expires_delta=datetime.timedelta(minutes=30)
    )
    return jsonify(access_token=access_token)


@app.route("/register", methods=["POST"])
def register():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user_exists = db_handler.check_user_exists(username)
    if user_exists:
        return jsonify({"msg": "user already exists"})
    else:
        db_handler.add_user_to_db(username, password)
        # additional_claims = {"username": username}
        # access_token = create_access_token(
        #     username, additional_claims=additional_claims
        # )
        access_token = create_access_token(
            username, expires_delta=datetime.timedelta(minutes=30)
        )
        return jsonify(access_token=access_token)


# @app.route("/books", methods=["GET", "POST"])
# def all_books():
#     response_object = {"status": "success"}

#     if request.method == "POST":
#         post_data = request.get_json()
#         BOOKS.append(
#             {
#                 "id": uuid.uuid4().hex,
#                 "title": post_data.get("title"),
#                 "author": post_data.get("author"),
#                 "read": post_data.get("read"),
#             }
#         )
#         response_object["message"] = "Book added!"
#     else:
#         response_object["books"] = BOOKS
#     return jsonify(response_object)


# @app.route("/books/<book_id>", methods=["PUT", "DELETE"])
# def single_book(book_id):
#     response_object = {"status": "success"}
#     if request.method == "PUT":
#         post_data = request.get_json()
#         remove_book(book_id)
#         BOOKS.append(
#             {
#                 "id": uuid.uuid4().hex,
#                 "title": post_data.get("title"),
#                 "author": post_data.get("author"),
#                 "read": post_data.get("read"),
#             }
#         )
#         response_object["message"] = "Book updated!"
#     if request.method == "DELETE":
#         remove_book(book_id)
#         response_object["message"] = "Book removed!"
#     return jsonify(response_object)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4794)
