# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: b53782d0b021a42afab7ceb31fb86f803bf6477731d41f6a5666caf0be4b79a4
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper


if TYPE_CHECKING:

    from . import int

    from . import vector2f



class Vector2i(_GraphWrapper):
    """A vector with two elements of Ints"""

    def execute(self, context):

        return self._inner.execute(context).as_vector2i()


    def vector2int_to_vector2float(self) -> vector2f.Vector2f:
        """Vector 2 Int to Vector 2 Float

        Given a Vector 2 Int. Creates a Vector 2 Float.
    
        Returns:
            Graph: A graph node producing a Vector2f.
        """
        vector_parsed = input_parsers.parse_graph(self)
        result = _internal.vector2_int_to_vector2_float_internal(vector_parsed)

        from .vector2f import Vector2f
        return Vector2f(result)

    def add(self, rhs) -> Vector2i:
        """Vector 2 Int Add

        Add two Vector 2s of Ints
    
        Args:
            rhs: Graph of Vector2i
            
    
        Returns:
            Graph: A graph node producing a Vector2i.
        """
        lhs_parsed = input_parsers.parse_graph(self)
        rhs_parsed = input_parsers.parse_graph(rhs)
        result = _internal.vector2i_add_internal(lhs_parsed, rhs_parsed)

        return Vector2i(result)

    @staticmethod
    def from_components(x, y) -> Vector2i:
        """Vector 2 Int from Components

        Given an x and y creates a vector.
    
        Args:
            x: Graph of Int
            y: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Vector2i.
        """
        x_parsed = input_parsers.parse_int_graph(x)
        y_parsed = input_parsers.parse_int_graph(y)
        result = _internal.vector2i_from_components_internal(x_parsed, y_parsed)

        return Vector2i(result)

    def passthrough(self) -> Vector2i:
        """Vector 2 Int Passthrough

        Responds with the value provided. Doing nothing to it.
    
        Returns:
            Graph: A graph node producing a Vector2i.
        """
        value_parsed = input_parsers.parse_graph(self)
        result = _internal.vector2i_passthrough_internal(value_parsed)

        return Vector2i(result)

    def to_vector2f(self) -> vector2f.Vector2f:
        """Vector 2 Int to Vector 2 Float

        Given a Vector 2 Int. Creates a Vector 2 Float.
    
        Returns:
            Graph: A graph node producing a Vector2f.
        """
        vector_parsed = input_parsers.parse_graph(self)
        result = _internal.vector2i_to_vector2f_internal(vector_parsed)

        from .vector2f import Vector2f
        return Vector2f(result)

    def x(self) -> int.Int:
        """Vector 2 Int get X

        Retrieves the X component of a Vector 2 Int.
    
        Returns:
            Graph: A graph node producing a Int.
        """
        vector_parsed = input_parsers.parse_graph(self)
        result = _internal.vector2i_x_internal(vector_parsed)

        from .int import Int
        return Int(result)

    def y(self) -> int.Int:
        """Vector 2 Int get Y

        Retrieves the Y component of a Vector 2 Int.
    
        Returns:
            Graph: A graph node producing a Int.
        """
        vector_parsed = input_parsers.parse_graph(self)
        result = _internal.vector2i_y_internal(vector_parsed)

        from .int import Int
        return Int(result)

