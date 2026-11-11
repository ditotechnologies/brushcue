# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 519f683412aad2a9ed81131e7b3874b6da311c6a765a7e8c78e9b01c451578d6
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import float
    from . import vector2f


class Point2f(Object):
    """A point with an x and y as floats"""

    def execute(self, context):
        return self._inner.execute(context)

    def add_vector(self, vector) -> Point2f:
        """Point 2 Float Add Vector 2 Float

        Offsets a Point 2 Float by a Vector 2 Float

        Args:
            vector: Graph of Vector2f

        Returns:
            Graph: A graph node producing a Point2f.
        """
        point_parsed = input_parsers.parse_graph(self)
        vector_parsed = input_parsers.parse_graph(vector)
        result = _internal.point2f_add_vector2f_internal(point_parsed, vector_parsed)
        return Point2f(result)

    def distance(self, rhs) -> float.Float:
        """Point 2 Float Distance

        The Euclidean distance between two Point 2 Floats.

        Args:
            rhs: Graph of Point2f

        Returns:
            Graph: A graph node producing a Float.
        """
        lhs_parsed = input_parsers.parse_graph(self)
        rhs_parsed = input_parsers.parse_graph(rhs)
        result = _internal.point2f_distance_internal(lhs_parsed, rhs_parsed)
        from .float import Float
        return Float(result)

    @staticmethod
    def from_components(x, y) -> Point2f:
        """Point 2 Float from Components

        Given an x and y creates a point

        Args:
            x: Graph of Float
            y: Graph of Float

        Returns:
            Graph: A graph node producing a Point2f.
        """
        x_parsed = input_parsers.parse_float_graph(x)
        y_parsed = input_parsers.parse_float_graph(y)
        result = _internal.point2f_from_components_internal(x_parsed, y_parsed)
        return Point2f(result)

    def subtract(self, rhs) -> vector2f.Vector2f:
        """Point 2 Float Subtract

        Subtracts two Point 2 Floats to produce the vector from rhs to lhs.

        Args:
            rhs: Graph of Point2f

        Returns:
            Graph: A graph node producing a Vector2f.
        """
        lhs_parsed = input_parsers.parse_graph(self)
        rhs_parsed = input_parsers.parse_graph(rhs)
        result = _internal.point2f_subtract_internal(lhs_parsed, rhs_parsed)
        from .vector2f import Vector2f
        return Vector2f(result)

    def x(self) -> float.Float:
        """Point 2 Float get X

        Retrieves the X component of a Point 2 Float.

        Returns:
            Graph: A graph node producing a Float.
        """
        point_parsed = input_parsers.parse_graph(self)
        result = _internal.point2f_x_internal(point_parsed)
        from .float import Float
        return Float(result)

    def y(self) -> float.Float:
        """Point 2 Float get Y

        Retrieves the Y component of a Point 2 Float.

        Returns:
            Graph: A graph node producing a Float.
        """
        point_parsed = input_parsers.parse_graph(self)
        result = _internal.point2f_y_internal(point_parsed)
        from .float import Float
        return Float(result)
