# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 3128d6461c9f05c083d8dbc5df56001fdd116968e6be8a0a11588f8cf1ccf517
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
    def if_(condition, then: _IfOutputT, otherwise: _IfOutputT) -> _IfOutputT:
        """If

        Selects one of two equally typed graph branches.

        Args:
            condition: Graph of Bool
            then: Graph of Any
            otherwise: Graph of Any

        Returns:
            Graph: A graph node producing a Any.
        """
        condition_parsed = input_parsers.parse_bool_graph(condition)
        then_parsed = input_parsers.parse_graph(then)
        otherwise_parsed = input_parsers.parse_graph(otherwise)
        input_parsers.ensure_same_graph_type(
            then,
            otherwise
            )
        result = _internal.if_internal(condition_parsed, then_parsed, otherwise_parsed)
        return input_parsers.resolve_output_graph(
            result,
            then,
            "Any",
        )
