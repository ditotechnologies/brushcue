import os

from . import _py
from ._graph import _GraphWrapper, unwrap_graph
from ._py import byte_list_constant_internal, image_from_byte_list_internal, composition_from_image_internal, int_constant_internal, float_constant_internal, string_constant_internal, bool_constant_internal

def parse_composition_graph(x) -> _py.Graph:
    if isinstance(x, (_GraphWrapper, _py.Graph)):
        return unwrap_graph(x)
    elif isinstance(x, bytes):
        byte_list_node = byte_list_constant_internal(x)
        image_node = image_from_byte_list_internal(byte_list_node)
        return composition_from_image_internal(image_node)
    elif isinstance(x, str):
        with open(x, "rb") as f:
            data = f.read()  # `data` is of type `bytes`
        byte_list_node = byte_list_constant_internal(data)
        image_node = image_from_byte_list_internal(byte_list_node)
        return composition_from_image_internal(image_node)
    else:
        raise TypeError(f"Expected Graph, str or bytes, got {type(x)}")

def parse_int_graph(x) -> _py.Graph:
    if isinstance(x, (_GraphWrapper, _py.Graph)):
        return unwrap_graph(x)
    elif isinstance(x, int):
        return int_constant_internal(x)
    else:
        raise TypeError(f"Expected Graph or int, got {type(x)}")

def parse_float_graph(x) -> _py.Graph:
    if isinstance(x, (_GraphWrapper, _py.Graph)):
        return unwrap_graph(x)
    elif isinstance(x, (float, int)):
        return float_constant_internal(float(x))
    else:
        raise TypeError(f"Expected Graph or float, got {type(x)}")

def parse_string_graph(x) -> _py.Graph:
    if isinstance(x, (_GraphWrapper, _py.Graph)):
        return unwrap_graph(x)
    elif isinstance(x, (str, os.PathLike)):
        return string_constant_internal(os.fspath(x))
    else:
        raise TypeError(f"Expected Graph, str or os.PathLike, got {type(x)}")

def parse_bool_graph(x) -> _py.Graph:
    if isinstance(x, (_GraphWrapper, _py.Graph)):
        return unwrap_graph(x)
    elif isinstance(x, bool):
        return bool_constant_internal(x)
    else:
        raise TypeError(f"Expected Graph or bool, got {type(x)}")

def parse_graph(x) -> _py.Graph:
    return unwrap_graph(x)
