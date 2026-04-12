from ._py import Graph, int_constant_internal, float_constant_internal, string_constant_internal, bool_constant_internal

def parse_int_graph(x) -> Graph:
    if isinstance(x, Graph):
        return x
    elif isinstance(x, int):
        return int_constant_internal(x)
    else:
        raise TypeError(f"Expected Graph or int, got {type(x)}")

def parse_float_graph(x) -> Graph:
    if isinstance(x, Graph):
        return x
    elif isinstance(x, (float, int)):
        return float_constant_internal(float(x))
    else:
        raise TypeError(f"Expected Graph or float, got {type(x)}")

def parse_string_graph(x) -> Graph:
    if isinstance(x, Graph):
        return x
    elif isinstance(x, str):
        return string_constant_internal(x)
    else:
        raise TypeError(f"Expected Graph or str, got {type(x)}")

def parse_bool_graph(x) -> Graph:
    if isinstance(x, Graph):
        return x
    elif isinstance(x, bool):
        return bool_constant_internal(x)
    else:
        raise TypeError(f"Expected Graph or bool, got {type(x)}")

def parse_graph(x) -> Graph:
    if isinstance(x, Graph):
        return x
    else:
        raise TypeError(f"Expected Graph, got {type(x)}")
