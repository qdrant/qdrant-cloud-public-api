"""
This file is used to store the configuration of the plugin - https://github.com/so1n/protobuf_to_pydantic
"""

import logging

logging.basicConfig(format="[%(asctime)s %(levelname)s] %(message)s", datefmt="%y-%m-%d %H:%M:%S", level=logging.INFO)


def default_func() -> None:
    return None

local_dict = {
    "default_func": default_func,
}

file_name_suffix = "_pydantic_schemas"
