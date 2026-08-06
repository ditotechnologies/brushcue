# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 111e46955e5b197e64c050268d646e276bf6797f689749f1797ffae2055d5d47
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper


if TYPE_CHECKING:

    from . import float



class Vector2f(_GraphWrapper):
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

    def passthrough(self) -> Vector2f:
        """Vector 2 Float Passthrough

        Responds with the value provided. Doing nothing to it.
    
        Returns:
            Graph: A graph node producing a Vector2f.
        """
        value_parsed = input_parsers.parse_graph(self)
        result = _internal.vector2f_passthrough_internal(value_parsed)

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

