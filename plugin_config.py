import logging

logging.basicConfig(format="[%(asctime)s %(levelname)s] %(message)s", datefmt="%y-%m-%d %H:%M:%S", level=logging.INFO)


def default_func() -> None:
    return None

local_dict = {
    "default_func": default_func,
}

file_name_suffix = "_pydantic_schemas"
