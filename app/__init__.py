from flask import Flask, jsonify, request
import os


from app.decorators import verify_keys, verify_type_values
from app.actions import register_new_user, get_users

app = Flask(__name__)

path_database = "database"
file_database_json = "database.json"
path_and_file = f"{path_database}/{file_database_json}"


if not os.path.isdir(path_database):
    os.mkdir(path_database)


@app.get("/")
def home():
    return {
        "message": "Bem vindo a entrega 8 - Flask + Exceções."
    }


@app.get("/user")
def user_get():
    return get_users(path_and_file)


@app.post("/user")
@verify_keys(["nome", "email"])
@verify_type_values
def user_post():
    request_json = request.get_json()
    return register_new_user(request_json, path_and_file)
