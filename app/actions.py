from app.read_file import read_file_and_transform_in_format_python, read_file_and_check_is_empty
from app.helpers import check_if_user_exist, create_file, generate_id, write_in_file, format_attributes_json, check_if_exist_file


def get_users(path_and_file: str):
    try:
        data: dict = {"data": []}
        if not check_if_exist_file(path_and_file):
            create_file(path_and_file, data)
            return data, 200

        elif (check_if_exist_file(path_and_file) and read_file_and_check_is_empty(path_and_file)):
            create_file(path_and_file, data)
            return data, 200

        return read_file_and_transform_in_format_python(path_and_file), 200
    except TypeError:
        return {"msg": "Erro ao retornar do banco procure suporte"}


def register_new_user(file_json: dict, path_file: str):
    try:
        data: dict = {"data": []}
        if not (check_if_exist_file(path_file)):
            create_file(path_file, data)
        elif (check_if_exist_file(path_file) and read_file_and_check_is_empty(path_file)):
            create_file(path_file, data)
        data_base_dict = read_file_and_transform_in_format_python(path_file)
        file_json = format_attributes_json(file_json)
        if (check_if_user_exist(file_json, data_base_dict['data'])):
            return {"error": "User already exists."}, 409
        file_json['id'] = generate_id(data_base_dict)
        data_base_dict['data'].append(file_json)
        write_in_file(path_file, data_base_dict)
        return file_json, 201
    except FileNotFoundError:
        return {"msg": "FileNotFoundError"}, 400
