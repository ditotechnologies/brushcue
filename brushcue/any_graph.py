# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: f78b954de8710bd2cc14263f52e684846fb2960f391866f8c5fe09f5e6d38ae5
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper

if TYPE_CHECKING:
    from .object import Object

_IfOutputT = TypeVar("_IfOutputT", bound="AnyGraph")


class AnyGraph(_GraphWrapper):
    """The common base for every typed graph value"""

    def execute(self, context):
        return self._inner.execute(context)

    @staticmethod
    def if_(condition, fn) -> _IfOutputT:
        """If

        Selects one of two equally typed graph branches.

        Args:
            condition: Graph of Bool
            fn: The function associated with this node.

        Returns:
            Graph: A graph node producing a Any.
        """
        condition_parsed = input_parsers.parse_bool_graph(condition)
        if not hasattr(fn, "__brushcue_make_graph__"):
            raise TypeError("fn must be annotated with @brushcue_fn")
        dispatched_graphs = fn.__brushcue_make_graph__([
            _internal.TypeDefinition.from_name("Any")
            ])
        input_parsers.ensure_same_graph_type(
            then,
            otherwise
            )
        result = _internal.if_internal(condition_parsed, *dispatched_graphs
            )

        return input_parsers.resolve_output_graph(
            result,
            fn.__brushcue_output_graph__,
            "Any",
        )
