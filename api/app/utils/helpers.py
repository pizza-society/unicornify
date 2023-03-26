""" API related helpers """
from typing import List, Union
import re



def to_camel_case(s: str) -> str:
    """
    Converts a snake_case string to camelCase.

    Args:
        s: The snake_case string to convert.

    Returns:
        The resulting camelCase string.
    """
    s = re.sub(r"_(?!_)([a-z])", lambda m: m.group(1).upper(), s)
    s = re.sub(r"_(?=_)", "", s)  # Remove consecutive underscores
    return s


def convert_snake_to_camel_dict_or_list(t_dict: Union[dict, List[dict]]) -> Union[dict, List[dict]]:
    """
    Recursively converts a dictionary or a list of dictionaries from snake_case to camelCase.

    Args:
        obj (dict or list): The object to be converted.

    Returns:
        dict or list: The converted object.
    """
    if isinstance(t_dict, list):
        return [convert_snake_to_camel_dict_or_list(i) if isinstance(i, (dict, list)) else i for i in t_dict]
    return {to_camel_case(a.lstrip('_')): convert_snake_to_camel_dict_or_list(b) if isinstance(b, (dict, list)) else b for a, b in t_dict.items()}