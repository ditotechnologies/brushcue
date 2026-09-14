# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 680f88fc2d63c365cd98a1e4b7ea0286938498e16334e52b75a471b1397107b5
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import bool
    from . import float


class Int(Object):
    """An integer"""

    def execute(self, context):
        return self._inner.execute(context).as_int()

    def abs(self) -> Int:
        """Int Absolute Value

        Returns the absolute value of an int

        Returns:
            Graph: A graph node producing a Int.
        """
        number_parsed = input_parsers.parse_int_graph(self)
        result = _internal.int_abs_internal(number_parsed)
        return Int(result)

    def add(self, int_2) -> Int:
        """Int Add

        Adds to ints together

        Args:
            int_2: Graph of Int

        Returns:
            Graph: A graph node producing a Int.
        """
        int_1_parsed = input_parsers.parse_int_graph(self)
        int_2_parsed = input_parsers.parse_int_graph(int_2)
        result = _internal.int_add_internal(int_1_parsed, int_2_parsed)
        return Int(result)

    def equals(self, int_2) -> bool.Bool:
        """Int Equals

        Checks if two ints are equal

        Args:
            int_2: Graph of Int

        Returns:
            Graph: A graph node producing a Bool.
        """
        int_1_parsed = input_parsers.parse_int_graph(self)
        int_2_parsed = input_parsers.parse_int_graph(int_2)
        result = _internal.int_equals_internal(int_1_parsed, int_2_parsed)
        from .bool import Bool
        return Bool(result)

    def greater_than(self, int_2) -> bool.Bool:
        """Int Greater Than

        Checks if the first int is greater than the second int

        Args:
            int_2: Graph of Int

        Returns:
            Graph: A graph node producing a Bool.
        """
        int_1_parsed = input_parsers.parse_int_graph(self)
        int_2_parsed = input_parsers.parse_int_graph(int_2)
        result = _internal.int_greater_than_internal(int_1_parsed, int_2_parsed)
        from .bool import Bool
        return Bool(result)

    def greater_than_or_equal(self, int_2) -> bool.Bool:
        """Int Greater Than Or Equal

        Checks if the first int is greater than or equal to the second int

        Args:
            int_2: Graph of Int

        Returns:
            Graph: A graph node producing a Bool.
        """
        int_1_parsed = input_parsers.parse_int_graph(self)
        int_2_parsed = input_parsers.parse_int_graph(int_2)
        result = _internal.int_greater_than_or_equal_internal(int_1_parsed, int_2_parsed)
        from .bool import Bool
        return Bool(result)

    def less_than(self, int_2) -> bool.Bool:
        """Int Less Than

        Checks if the first int is less than the second int

        Args:
            int_2: Graph of Int

        Returns:
            Graph: A graph node producing a Bool.
        """
        int_1_parsed = input_parsers.parse_int_graph(self)
        int_2_parsed = input_parsers.parse_int_graph(int_2)
        result = _internal.int_less_than_internal(int_1_parsed, int_2_parsed)
        from .bool import Bool
        return Bool(result)

    def less_than_or_equal(self, int_2) -> bool.Bool:
        """Int Less Than Or Equal

        Checks if the first int is less than or equal to the second int

        Args:
            int_2: Graph of Int

        Returns:
            Graph: A graph node producing a Bool.
        """
        int_1_parsed = input_parsers.parse_int_graph(self)
        int_2_parsed = input_parsers.parse_int_graph(int_2)
        result = _internal.int_less_than_or_equal_internal(int_1_parsed, int_2_parsed)
        from .bool import Bool
        return Bool(result)

    def max(self, int2) -> Int:
        """Int Max

        Returns the maximum int.

        Args:
            int2: Graph of Int

        Returns:
            Graph: A graph node producing a Int.
        """
        int1_parsed = input_parsers.parse_int_graph(self)
        int2_parsed = input_parsers.parse_int_graph(int2)
        result = _internal.int_max_internal(int1_parsed, int2_parsed)
        return Int(result)

    def min(self, int2) -> Int:
        """Int Min

        Returns the minimum int.

        Args:
            int2: Graph of Int

        Returns:
            Graph: A graph node producing a Int.
        """
        int1_parsed = input_parsers.parse_int_graph(self)
        int2_parsed = input_parsers.parse_int_graph(int2)
        result = _internal.int_min_internal(int1_parsed, int2_parsed)
        return Int(result)

    def multiply(self, int_2) -> Int:
        """Int Multiply

        Multiplies two integers together

        Args:
            int_2: Graph of Int

        Returns:
            Graph: A graph node producing a Int.
        """
        int_1_parsed = input_parsers.parse_int_graph(self)
        int_2_parsed = input_parsers.parse_int_graph(int_2)
        result = _internal.int_multiply_internal(int_1_parsed, int_2_parsed)
        return Int(result)

    def subtract(self, int_2) -> Int:
        """Int Subtract

        Subtracts one int from another

        Args:
            int_2: Graph of Int

        Returns:
            Graph: A graph node producing a Int.
        """
        int_1_parsed = input_parsers.parse_int_graph(self)
        int_2_parsed = input_parsers.parse_int_graph(int_2)
        result = _internal.int_subtract_internal(int_1_parsed, int_2_parsed)
        return Int(result)

    def to_float(self) -> float.Float:
        """Int To Float

        Converts an Int to a Float

        Returns:
            Graph: A graph node producing a Float.
        """
        int_parsed = input_parsers.parse_int_graph(self)
        result = _internal.int_to_float_internal(int_parsed)
        from .float import Float
        return Float(result)
