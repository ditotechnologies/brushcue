from functools import wraps

import brushcue

from ._graph import unwrap_graph


def brushcue_fn(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    def brushcue_make_graph(
            type_definitions: list[brushcue.TypeDefinition],
    ):
        inputs = [
            brushcue.Object.input(type_definition)
            for type_definition in type_definitions
        ]
        output = fn(*inputs)
        wrapper.__brushcue_output_graph__ = output
        return *(unwrap_graph(graph) for graph in inputs), unwrap_graph(output)

    wrapper.__brushcue_make_graph__ = brushcue_make_graph
    return wrapper
