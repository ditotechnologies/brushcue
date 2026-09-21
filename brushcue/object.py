# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: f5e89f0e2e932da0e04fcf9e0a4f7a9afdc03204c850770a19ce43347573520c
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Self

from . import _py as _internal, input_parsers
from .any_graph import AnyGraph

if TYPE_CHECKING:
    from . import list
    from . import stream


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

    def to_stream(self) -> stream.Stream:
        """Object to Stream

        Converts an object to a stream

        Returns:
            Graph: A graph node producing a Stream.
        """
        object_parsed = input_parsers.parse_graph(self)
        result = _internal.object_to_stream_internal(object_parsed)
        return input_parsers.resolve_output_graph(
            result,
            self,
            "Stream",
        )
