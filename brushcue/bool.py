# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: aff8e8b2b8a0a87efc20fa64aaa3613ee09be98f12dfd8fe741659b15d374962
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    import builtins


class Bool(Object):
    """A bool"""

    def execute(self, context):
        return self._inner.execute(context).as_bool()

    if TYPE_CHECKING:
        # Implemented at runtime via monkeypatching in `_operators.py`; declared
        # here only so static type checkers recognize these operators.
        def __and__(self, other: Bool | builtins.bool) -> Bool: ...
        def __rand__(self, other: Bool | builtins.bool) -> Bool: ...
        def __or__(self, other: Bool | builtins.bool) -> Bool: ...
        def __ror__(self, other: Bool | builtins.bool) -> Bool: ...
        def __xor__(self, other: Bool | builtins.bool) -> Bool: ...
        def __rxor__(self, other: Bool | builtins.bool) -> Bool: ...
        def __invert__(self) -> Bool: ...

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
