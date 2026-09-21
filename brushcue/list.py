# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: b1ffd3e88ce4c1032bc5f03876af5a476d69e389d7e028fcab2edfbf2b399ddc
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar

from . import _py as _internal, input_parsers
from .any_graph import AnyGraph

if TYPE_CHECKING:
    from .object import Object
    from . import stream

_ListItemT = TypeVar("_ListItemT", bound="Object")


class List(AnyGraph, Generic[_ListItemT]):
    """A generic list in the graph"""

    def execute(self, context):
        return self._inner.execute(context)

    def append(self, element) -> List[_ListItemT]:
        """List Append

        Appends an element to a list

        Args:
            element: Graph of Object

        Returns:
            Graph: A graph node producing a List.
        """
        list_parsed = input_parsers.parse_graph(self)
        element_parsed = input_parsers.parse_graph(element)
        result = _internal.list_append_internal(list_parsed, element_parsed)
        return input_parsers.resolve_output_graph(
            result,
            self,
            "List",
        )

    def first(self) -> _ListItemT:
        """List First

        Returns the first element of a list

        Returns:
            Graph: A graph node producing a Object.
        """
        list_parsed = input_parsers.parse_graph(self)
        result = _internal.list_first_internal(list_parsed)
        return input_parsers.resolve_output_graph(
            result,
            self,
            "Object",
        )

    def to_stream(self) -> stream.Stream:
        """List to Stream

        Converts a list to a stream

        Returns:
            Graph: A graph node producing a Stream.
        """
        list_parsed = input_parsers.parse_graph(self)
        result = _internal.list_to_stream_internal(list_parsed)
        return input_parsers.resolve_output_graph(
            result,
            self,
            "Stream",
        )
