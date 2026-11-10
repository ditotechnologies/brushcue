# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: ed3d9aa73b15d90109008d5c3b43ba42bb14a0145e39798086bdb60ea321a3b9
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Self

from . import _py as _internal, input_parsers
from .any_graph import AnyGraph

if TYPE_CHECKING:
    from . import list


class Object(AnyGraph):
    """An object whose concrete graph type is determined by context"""

    def execute(self, context):
        return self._inner.execute(context)

    @staticmethod
    def input(output_type: _internal.TypeDefinition) -> AnyGraph:
        """Create a dispatched input with an explicit graph output type."""
        result = _internal.input_internal(output_type)
        return input_parsers.wrap_graph_for_type_definition(result, output_type)

    def to_list(self) -> list.List:
        """Object to List

        Converts an object to a list

        Returns:
            Graph: A graph node producing a List.
        """
        object_parsed = input_parsers.parse_graph(self)
        result = _internal.object_to_list_internal(object_parsed)
        return input_parsers.resolve_output_graph(
            result,
            self,
            "List",
        )
