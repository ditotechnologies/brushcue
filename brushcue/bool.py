# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: b3fc5ae76ea339f9fcaaf00064360e5da3b2353edc5f88254159049aeab1ce21
# generated from templates/py_type.jinja

from __future__ import annotations

from . import _py as _internal, input_parsers
from .object import Object


class Bool(Object):
    """A bool"""

    def execute(self, context):
        return self._inner.execute(context).as_bool()

    def and_(self, bool2) -> Bool:
        """And

        Returns true if both inputs are true.

        Args:
            bool2: Graph of Bool

        Returns:
            Graph: A graph node producing a Bool.
        """
        bool1_parsed = input_parsers.parse_bool_graph(self)
        bool2_parsed = input_parsers.parse_bool_graph(bool2)
        result = _internal.and_internal(bool1_parsed, bool2_parsed)
        return Bool(result)

    def not_(self) -> Bool:
        """Not

        Returns the opposite of a boolean

        Returns:
            Graph: A graph node producing a Bool.
        """
        bool_parsed = input_parsers.parse_bool_graph(self)
        result = _internal.not_internal(bool_parsed)
        return Bool(result)

    def or_(self, bool2) -> Bool:
        """Or

        Returns true if either inputs are true.

        Args:
            bool2: Graph of Bool

        Returns:
            Graph: A graph node producing a Bool.
        """
        bool1_parsed = input_parsers.parse_bool_graph(self)
        bool2_parsed = input_parsers.parse_bool_graph(bool2)
        result = _internal.or_internal(bool1_parsed, bool2_parsed)
        return Bool(result)

    def xor(self, bool2) -> Bool:
        """Exclusive Or

        Returns true if either the inputs are true. But false if both are true.

        Args:
            bool2: Graph of Bool

        Returns:
            Graph: A graph node producing a Bool.
        """
        bool1_parsed = input_parsers.parse_bool_graph(self)
        bool2_parsed = input_parsers.parse_bool_graph(bool2)
        result = _internal.xor_internal(bool1_parsed, bool2_parsed)
        return Bool(result)
