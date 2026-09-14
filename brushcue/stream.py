# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: d694c0d49307404a4aec574c595d908fa2b2983a15e5940fa07a3c752c01751d
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar

from . import _py as _internal, input_parsers
from .any_graph import AnyGraph

if TYPE_CHECKING:
    from .object import Object
    from . import list

_StreamItemT = TypeVar("_StreamItemT", bound="Object")
_StreamMapOutputT = TypeVar("_StreamMapOutputT", bound="Object")


class Stream(AnyGraph, Generic[_StreamItemT]):
    """A generic stream in the graph"""

    def execute(self, context):
        return self._inner.execute(context)

    def collect(self) -> list.List[_StreamItemT]:
        """Stream Collect

        Collects a stream into a list

        Returns:
            Graph: A graph node producing a List.
        """
        stream_parsed = input_parsers.parse_graph(self)
        result = _internal.stream_collect_internal(stream_parsed)
        return input_parsers.resolve_output_graph(
            result,
            self,
            "List",
        )

    def filter(self, item, output) -> Stream[_StreamItemT]:
        """Stream Filter

        Performs a filter operation over a stream

        Args:
            item: Graph of Object
            output: Graph of Bool

        Returns:
            Graph: A graph node producing a Stream.
        """
        stream_parsed = input_parsers.parse_graph(self)
        item_parsed = input_parsers.parse_graph(item)
        output_parsed = input_parsers.parse_bool_graph(output)
        result = _internal.stream_filter_internal(stream_parsed, item_parsed, output_parsed)
        return input_parsers.resolve_output_graph(
            result,
            self,
            "Stream",
        )

    def first(self) -> _StreamItemT:
        """Stream First

        Returns the first element of a stream

        Returns:
            Graph: A graph node producing a Object.
        """
        stream_parsed = input_parsers.parse_graph(self)
        result = _internal.stream_first_internal(stream_parsed)
        return input_parsers.resolve_output_graph(
            result,
            self,
            "Object",
        )

    def map(self, item, output: _StreamMapOutputT) -> Stream[_StreamMapOutputT]:
        """Stream Map

        Performs a map operation over a stream

        Args:
            item: Graph of Object
            output: Graph of Object

        Returns:
            Graph: A graph node producing a Stream.
        """
        stream_parsed = input_parsers.parse_graph(self)
        item_parsed = input_parsers.parse_graph(item)
        output_parsed = input_parsers.parse_graph(output)
        result = _internal.stream_map_internal(stream_parsed, item_parsed, output_parsed)
        return input_parsers.resolve_output_graph(
            result,
            output,
            "Stream",
        )
