import os
from datetime import timedelta
from flask import (
    Flask,
    jsonify,
    request,
    session,
    render_template_string,
    redirect,
    url_for,
)
from flask_cors import CORS
import uuid
from db.db_handler import DBHandler

# configuration
DEBUG = True


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = os.environ["finance_app_secret_key"]
# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

db_handler = DBHandler()


@app.route("/set/")
def set():
    session["key"] = "value"
    return "ok"


@app.route("/get/")
def get():
    return session.get("key", "not set")


# # sanity check route
# @app.route("/ping", methods=["GET"])
# def ping_pong():
#     return jsonify("pong!")


@app.route("/", methods=["GET"])
def home():
    response_object = {"status": "success"}
    db_conn = db_handler.get_db_connection()
    users = db_handler.get_all_elements_from_table(db_conn, "user")
    response_object["users"] = users
    return jsonify(response_object)


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
