from ujson import load


def read_file_and_return_str(file_path: str) -> str:
    with open(file_path, "r") as f:
        new_file = f.read()
    return new_file


def read_file_and_transform_in_format_python(file_path: str):
    with open(file_path, "r") as file_format_in_python:
        new_file = load(file_format_in_python)
    return new_file


def read_file_and_check_is_empty(file_path: str):
    try:
        file = read_file_and_transform_in_format_python(file_path)
        return False if file else True
    except ValueError:
        return True
