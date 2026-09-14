# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 608e9e9c37d8d79431512d7e8bf71657ff8dc9067053e56cf583c476e26fac9b
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import bool
    from . import int


class Float(Object):
    """A float"""

    def execute(self, context):
        return self._inner.execute(context).as_float()

    def abs(self) -> Float:
        """Absolute Value

        Returns the absolute value of a float

        Returns:
            Graph: A graph node producing a Float.
        """
        number_parsed = input_parsers.parse_float_graph(self)
        result = _internal.abs_internal(number_parsed)
        return Float(result)

    def add(self, float2) -> Float:
        """Float Add

        Adds two floats together.

        Args:
            float2: Graph of Float

        Returns:
            Graph: A graph node producing a Float.
        """
        float1_parsed = input_parsers.parse_float_graph(self)
        float2_parsed = input_parsers.parse_float_graph(float2)
        result = _internal.float_add_internal(float1_parsed, float2_parsed)
        return Float(result)

    def cos(self) -> Float:
        """Float Cosine

        Computes the cosine of a float (in radians).

        Returns:
            Graph: A graph node producing a Float.
        """
        angle_parsed = input_parsers.parse_float_graph(self)
        result = _internal.float_cos_internal(angle_parsed)
        return Float(result)

    def divide(self, float2) -> Float:
        """Float Divide

        Adds two floats together.

        Args:
            float2: Graph of Float

        Returns:
            Graph: A graph node producing a Float.
        """
        float1_parsed = input_parsers.parse_float_graph(self)
        float2_parsed = input_parsers.parse_float_graph(float2)
        result = _internal.float_divide_internal(float1_parsed, float2_parsed)
        return Float(result)

    def equals(self, float_2) -> bool.Bool:
        """Float Equals

        Checks if two floats are equal

        Args:
            float_2: Graph of Float

        Returns:
            Graph: A graph node producing a Bool.
        """
        float_1_parsed = input_parsers.parse_float_graph(self)
        float_2_parsed = input_parsers.parse_float_graph(float_2)
        result = _internal.float_equals_internal(float_1_parsed, float_2_parsed)
        from .bool import Bool
        return Bool(result)

    def greater_than(self, float_2) -> bool.Bool:
        """Float Greater Than

        Checks if the first float is greater than the second float

        Args:
            float_2: Graph of Float

        Returns:
            Graph: A graph node producing a Bool.
        """
        float_1_parsed = input_parsers.parse_float_graph(self)
        float_2_parsed = input_parsers.parse_float_graph(float_2)
        result = _internal.float_greater_than_internal(float_1_parsed, float_2_parsed)
        from .bool import Bool
        return Bool(result)

    def greater_than_or_equal(self, float_2) -> bool.Bool:
        """Float Greater Than Or Equal

        Checks if the first float is greater than or equal to the second float

        Args:
            float_2: Graph of Float

        Returns:
            Graph: A graph node producing a Bool.
        """
        float_1_parsed = input_parsers.parse_float_graph(self)
        float_2_parsed = input_parsers.parse_float_graph(float_2)
        result = _internal.float_greater_than_or_equal_internal(float_1_parsed, float_2_parsed)
        from .bool import Bool
        return Bool(result)

    def lerp(self, float1, float2) -> Float:
        """Float Lerp

        Lerps between two floats using the x parameter

        Args:
            float1: Graph of Float
            float2: Graph of Float

        Returns:
            Graph: A graph node producing a Float.
        """
        x_parsed = input_parsers.parse_float_graph(self)
        float1_parsed = input_parsers.parse_float_graph(float1)
        float2_parsed = input_parsers.parse_float_graph(float2)
        result = _internal.float_lerp_internal(x_parsed, float1_parsed, float2_parsed)
        return Float(result)

    def less_than(self, float_2) -> bool.Bool:
        """Float Less Than

        Checks if the first float is less than the second float

        Args:
            float_2: Graph of Float

        Returns:
            Graph: A graph node producing a Bool.
        """
        float_1_parsed = input_parsers.parse_float_graph(self)
        float_2_parsed = input_parsers.parse_float_graph(float_2)
        result = _internal.float_less_than_internal(float_1_parsed, float_2_parsed)
        from .bool import Bool
        return Bool(result)

    def less_than_or_equal(self, float_2) -> bool.Bool:
        """Float Less Than Or Equal

        Checks if the first float is less than or equal to the second float

        Args:
            float_2: Graph of Float

        Returns:
            Graph: A graph node producing a Bool.
        """
        float_1_parsed = input_parsers.parse_float_graph(self)
        float_2_parsed = input_parsers.parse_float_graph(float_2)
        result = _internal.float_less_than_or_equal_internal(float_1_parsed, float_2_parsed)
        from .bool import Bool
        return Bool(result)

    def max(self, float2) -> Float:
        """Float Max

        Returns the maximum float.

        Args:
            float2: Graph of Float

        Returns:
            Graph: A graph node producing a Float.
        """
        float1_parsed = input_parsers.parse_float_graph(self)
        float2_parsed = input_parsers.parse_float_graph(float2)
        result = _internal.float_max_internal(float1_parsed, float2_parsed)
        return Float(result)

    def min(self, float2) -> Float:
        """Float Min

        Returns the minimum float.

        Args:
            float2: Graph of Float

        Returns:
            Graph: A graph node producing a Float.
        """
        float1_parsed = input_parsers.parse_float_graph(self)
        float2_parsed = input_parsers.parse_float_graph(float2)
        result = _internal.float_min_internal(float1_parsed, float2_parsed)
        return Float(result)

    def multiply(self, float2) -> Float:
        """Float Multiply

        Multiplies two floats together.

        Args:
            float2: Graph of Float

        Returns:
            Graph: A graph node producing a Float.
        """
        float1_parsed = input_parsers.parse_float_graph(self)
        float2_parsed = input_parsers.parse_float_graph(float2)
        result = _internal.float_multiply_internal(float1_parsed, float2_parsed)
        return Float(result)

    def pow(self, float2) -> Float:
        """Float Power

        Raises float 1 to the power of float 2

        Args:
            float2: Graph of Float

        Returns:
            Graph: A graph node producing a Float.
        """
        float1_parsed = input_parsers.parse_float_graph(self)
        float2_parsed = input_parsers.parse_float_graph(float2)
        result = _internal.float_pow_internal(float1_parsed, float2_parsed)
        return Float(result)

    def round_to_int(self) -> int.Int:
        """Float Round to Int

        Rounds the float to the nearest int

        Returns:
            Graph: A graph node producing a Int.
        """
        float_parsed = input_parsers.parse_float_graph(self)
        result = _internal.float_round_to_int_internal(float_parsed)
        from .int import Int
        return Int(result)

    def sin(self) -> Float:
        """Float Sine

        Computes the sine of a float (in radians).

        Returns:
            Graph: A graph node producing a Float.
        """
        angle_parsed = input_parsers.parse_float_graph(self)
        result = _internal.float_sin_internal(angle_parsed)
        return Float(result)

    def square_root(self) -> Float:
        """Float Square Root

        Compares the square root of a number

        Returns:
            Graph: A graph node producing a Float.
        """
        number_parsed = input_parsers.parse_float_graph(self)
        result = _internal.float_square_root_internal(number_parsed)
        return Float(result)

    def squared(self) -> Float:
        """Float Squared

        Raises a float to the power of 2.

        Returns:
            Graph: A graph node producing a Float.
        """
        number_parsed = input_parsers.parse_float_graph(self)
        result = _internal.float_squared_internal(number_parsed)
        return Float(result)

    def subtract(self, float2) -> Float:
        """Float Subtract

        Adds two floats together.

        Args:
            float2: Graph of Float

        Returns:
            Graph: A graph node producing a Float.
        """
        float1_parsed = input_parsers.parse_float_graph(self)
        float2_parsed = input_parsers.parse_float_graph(float2)
        result = _internal.float_subtract_internal(float1_parsed, float2_parsed)
        return Float(result)

    @staticmethod
    def pi() -> Float:
        """Pi

        Returns π as a float

        Returns:
            Graph: A graph node producing a Float.
        """
        result = _internal.pi_internal()
        return Float(result)
