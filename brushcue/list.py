# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 17e2553162c2ca6be552a79d5552bd4eea30a686c345696f8bff8c39203a4a66
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar

from . import _py as _internal, input_parsers
from .any_graph import AnyGraph

if TYPE_CHECKING:
    from .object import Object
    from . import int

_ListItemT = TypeVar("_ListItemT", bound="Object")
_ListFoldOutputT = TypeVar("_ListFoldOutputT", bound="Object")
_ListMapOutputT = TypeVar("_ListMapOutputT", bound="Object")


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

    def filter(self, fn) -> List[_ListItemT]:
        """List Filter

        Keeps the elements of a list for which a function returns true

        Args:
            fn: The function associated with this node.

        Returns:
            Graph: A graph node producing a List.
        """
        list_parsed = input_parsers.parse_graph(self)
        if not hasattr(fn, "__brushcue_make_graph__"):
            raise TypeError("fn must be annotated with @brushcue_fn")
        dispatched_graphs = fn.__brushcue_make_graph__([
            _internal.TypeDefinition.from_name(self._resolved_type.__name__)
            ])
        result = _internal.list_filter_internal(list_parsed, *dispatched_graphs
            )

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

    def fold(self, initial_accumulator: _ListFoldOutputT, fn) -> _ListFoldOutputT:
        """List Fold

        Folds the elements of a list into an accumulator

        Args:
            initial_accumulator: Graph of Object
            fn: The function associated with this node.

        Returns:
            Graph: A graph node producing a Object.
        """
        list_parsed = input_parsers.parse_graph(self)
        initial_accumulator_parsed = input_parsers.parse_graph(initial_accumulator)
        if not hasattr(fn, "__brushcue_make_graph__"):
            raise TypeError("fn must be annotated with @brushcue_fn")
        dispatched_graphs = fn.__brushcue_make_graph__([
            _internal.TypeDefinition.from_name("Object"),
            _internal.TypeDefinition.from_name(self._resolved_type.__name__)
            ])
        result = _internal.list_fold_internal(list_parsed, initial_accumulator_parsed, *dispatched_graphs
            )

        return input_parsers.resolve_output_graph(
            result,
            initial_accumulator,
            "Object",
        )

    def get(self, index) -> _ListItemT:
        """List Get

        Fetches the element of the list at a given index.

        Args:
            index: Graph of Int

        Returns:
            Graph: A graph node producing a Object.
        """
        list_parsed = input_parsers.parse_graph(self)
        index_parsed = input_parsers.parse_int_graph(index)
        result = _internal.list_get_internal(list_parsed, index_parsed)
        return input_parsers.resolve_output_graph(
            result,
            self,
            "Object",
        )

    def length(self) -> int.Int:
        """List Length

        Returns the number of elements in a list.

        Returns:
            Graph: A graph node producing a Int.
        """
        list_parsed = input_parsers.parse_graph(self)
        result = _internal.list_length_internal(list_parsed)
        from .int import Int
        return Int(result)

    def map(self, fn) -> List[_ListMapOutputT]:
        """List Map

        Applies a function to every element of a list

        Args:
            fn: The function associated with this node.

        Returns:
            Graph: A graph node producing a List.
        """
        list_parsed = input_parsers.parse_graph(self)
        if not hasattr(fn, "__brushcue_make_graph__"):
            raise TypeError("fn must be annotated with @brushcue_fn")
        dispatched_graphs = fn.__brushcue_make_graph__([
            _internal.TypeDefinition.from_name(self._resolved_type.__name__)
            ])
        result = _internal.list_map_internal(list_parsed, *dispatched_graphs
            )

        return input_parsers.resolve_output_graph(
            result,
            fn.__brushcue_output_graph__,
            "List",
        )
