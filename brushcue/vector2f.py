# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 1a6a1b8fc53cb2843a77a47ac2da31e723800b05b46bdd9fdb2b6b71bccb175b
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import float


class Vector2f(Object):
    """A vector with two elements of Floats"""

    def execute(self, context):
        return self._inner.execute(context).as_vector2f()

    def add(self, rhs) -> Vector2f:
        """Vector 2 Float Add

        Add two Vector 2s of Floats

        Args:
            rhs: Graph of Vector2f

        Returns:
            Graph: A graph node producing a Vector2f.
        """
        lhs_parsed = input_parsers.parse_graph(self)
        rhs_parsed = input_parsers.parse_graph(rhs)
        result = _internal.vector2f_add_internal(lhs_parsed, rhs_parsed)
        return Vector2f(result)

    @staticmethod
    def from_components(x, y) -> Vector2f:
        """Vector 2 Float from Components

        Given an x and y creates a vector.

        Args:
            x: Graph of Float
            y: Graph of Float

        Returns:
            Graph: A graph node producing a Vector2f.
        """
        x_parsed = input_parsers.parse_float_graph(x)
        y_parsed = input_parsers.parse_float_graph(y)
        result = _internal.vector2f_from_components_internal(x_parsed, y_parsed)
        return Vector2f(result)

    def normalize(self) -> Vector2f:
        """Vector 2 Float Normalize

        Normalizes a Vector. Converting it's length to 1.

        Returns:
            Graph: A graph node producing a Vector2f.
        """
        vector_parsed = input_parsers.parse_graph(self)
        result = _internal.vector2f_normalize_internal(vector_parsed)
        return Vector2f(result)

    def scalar_multiply(self, scalar) -> Vector2f:
        """Vector 2 Float Scalar Multiply

        Multiplies each element of the Vector as a scalar

        Args:
            scalar: Graph of Float

        Returns:
            Graph: A graph node producing a Vector2f.
        """
        vector_parsed = input_parsers.parse_graph(self)
        scalar_parsed = input_parsers.parse_float_graph(scalar)
        result = _internal.vector2f_scalar_multiply_internal(vector_parsed, scalar_parsed)
        return Vector2f(result)

    def x(self) -> float.Float:
        """Vector 2 Float get X

        Retrieves the X component of a Vector 2 Float.

        Returns:
            Graph: A graph node producing a Float.
        """
        vector_parsed = input_parsers.parse_graph(self)
        result = _internal.vector2f_x_internal(vector_parsed)
        from .float import Float
        return Float(result)

    def y(self) -> float.Float:
        """Vector 2 Float get Y

        Retrieves the Y component of a Vector 2 Float.

        Returns:
            Graph: A graph node producing a Float.
        """
        vector_parsed = input_parsers.parse_graph(self)
        result = _internal.vector2f_y_internal(vector_parsed)
        from .float import Float
        return Float(result)
