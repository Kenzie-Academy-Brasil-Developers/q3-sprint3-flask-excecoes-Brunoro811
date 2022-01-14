from ujson import dump
import os


def check_if_user_exist(user: dict, data: dict) -> bool:
    for element in data:
        print(
            f"{element['email']} == {user['email']} => {True if (element['email'] == user['email']) else False}")
        if (element['email'] == user['email']):
            return True
    return False


def check_if_exist_file(file_path: str) -> bool:
    if os.path.isfile(file_path):
        return True
    return False


def format_attributes_json(file_json: dict) -> dict:
    try:
        file_json['nome'] = file_json['nome'].title()
        file_json['email'] = file_json['email'].lower()
        return file_json
    except KeyError:
        return {
            "msg": "Chave(s) invalida(s)",
            "received": file_json
        }, 400


def generate_id(data_base: dict) -> int:
    las_id = 0
    data_base = data_base['data']
    if data_base:
        las_element = data_base[len(data_base)-1]
        las_id = las_element['id']
    return las_id + 1


def create_file(file_path: str, writer: dict) -> tuple:
    with open(file_path, "w") as json_file:
        dump(writer, json_file, indent=2)
    return writer, 201


def write_in_file(file_path: str, dict_writer: dict) -> tuple:
    with open(file_path, "w") as json_file:
        dump(dict_writer, json_file, indent=2)
    return dict_writer, 201


def get_types_dict(data: dict):
    nome = "nome"
    email = "email"
    types_in_language_human: list = [
        "string", "integer", "float", "boolean", "list", "dictionary"]
    for i in range(0, len(types_in_language_human)):

        if type(data['nome']) == str:
            nome = "string"
        elif type(data['nome']) == int:
            nome = "integer"
        elif type(data['nome']) == float:
            nome = "float"
        elif type(data['nome']) == bool:
            nome = "boolean"
        elif type(data['nome']) == list:
            nome = "list"
        elif type(data['nome']) == dict:
            nome = "dictionary"

        if type(data['email']) == str:
            email = "string"
        elif type(data['email']) == int:
            email = "integer"
        elif type(data['email']) == float:
            email = "float"
        elif type(data['email']) == bool:
            email = "boolean"
        elif type(data['email']) == list:
            email = "list"
        elif type(data['email']) == dict:
            email = "dictionary"

    return {
        "nome": nome,
        "email": email
    }
