from functools import wraps
from flask import request

from app.helpers import get_types_dict


def verify_keys(trusted_keys: list[str]):
    def received_function(func):
        @wraps(func)
        def wrapper():
            request_json = request.get_json()
            trusted_keys.sort()
            try:
                password = request_json[trusted_keys[0]]
                username = request_json[trusted_keys[1]]
                return func()
            except KeyError:
                return {
                    "error": "chave(s) incorreta(s)",
                    "expected": [
                        "nome",
                        "email"
                    ],
                    "received": list(request_json.keys())
                }, 400
        return wrapper
    return received_function


def verify_type_values(func):
    @wraps(func)
    def wrapper():
        request_json = request.get_json()
        values_list = list(request_json.values())

        if type(values_list[0]) != str or type(values_list[1]) != str:
            request_json = get_types_dict(request_json)
            return {
                "wrong fields": [
                    {
                        "nome": f"{request_json['nome']}"
                    },
                    {
                        "email": f"{request_json['email']}"
                    }
                ]
            }, 400
        return func()
    return wrapper
