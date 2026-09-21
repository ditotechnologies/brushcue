# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: d63f184239c1f1329ec246c9e4d5fa19828313c82ed6515ea90fc641ec2a894b
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar

from . import _py as _internal, input_parsers
from .any_graph import AnyGraph

if TYPE_CHECKING:
    from .object import Object
    from . import list

_StreamItemT = TypeVar("_StreamItemT", bound="Object")
_StreamFoldOutputT = TypeVar("_StreamFoldOutputT", bound="Object")
_StreamMapOutputT = TypeVar("_StreamMapOutputT", bound="Object")


class Stream(AnyGraph, Generic[_StreamItemT]):
    """A generic stream in the graph"""

    def execute(self, context):
        return self._inner.execute(context)

    def collect(self) -> list.List:
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

    def filter(self, fn) -> Stream[_StreamItemT]:
        """Stream Filter

        Performs a filter operation over a stream

        Args:
            fn: The function associated with this node.

        Returns:
            Graph: A graph node producing a Stream.
        """
        stream_parsed = input_parsers.parse_graph(self)
        if not hasattr(fn, "__brushcue_make_graph__"):
            raise TypeError("fn must be annotated with @brushcue_fn")
        dispatched_graphs = fn.__brushcue_make_graph__([
            _internal.TypeDefinition.from_name(self._resolved_type.__name__)
            ])
        result = _internal.stream_filter_internal(stream_parsed, *dispatched_graphs
            )

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

    def fold(self, initial_accumulator: _StreamFoldOutputT, fn) -> _StreamFoldOutputT:
        """Stream Fold

        Folds the elements of a stream into an accumulator

        Args:
            initial_accumulator: Graph of Object
            fn: The function associated with this node.

        Returns:
            Graph: A graph node producing a Object.
        """
        stream_parsed = input_parsers.parse_graph(self)
        initial_accumulator_parsed = input_parsers.parse_graph(initial_accumulator)
        if not hasattr(fn, "__brushcue_make_graph__"):
            raise TypeError("fn must be annotated with @brushcue_fn")
        dispatched_graphs = fn.__brushcue_make_graph__([
            _internal.TypeDefinition.from_name("Object"),
            _internal.TypeDefinition.from_name(self._resolved_type.__name__)
            ])
        result = _internal.stream_fold_internal(stream_parsed, initial_accumulator_parsed, *dispatched_graphs
            )

        return input_parsers.resolve_output_graph(
            result,
            initial_accumulator,
            "Object",
        )

    def map(self, fn) -> Stream[_StreamMapOutputT]:
        """Stream Map

        Performs a map operation over a stream

        Args:
            fn: The function associated with this node.

        Returns:
            Graph: A graph node producing a Stream.
        """
        stream_parsed = input_parsers.parse_graph(self)
        if not hasattr(fn, "__brushcue_make_graph__"):
            raise TypeError("fn must be annotated with @brushcue_fn")
        dispatched_graphs = fn.__brushcue_make_graph__([
            _internal.TypeDefinition.from_name(self._resolved_type.__name__)
            ])
        result = _internal.stream_map_internal(stream_parsed, *dispatched_graphs
            )

        return input_parsers.resolve_output_graph(
            result,
            fn.__brushcue_output_graph__,
            "Stream",
        )
