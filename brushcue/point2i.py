# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: e3cd76933dcf69199abaa02e6d36980b582328e74d765681173c17abb9530d47
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper


if TYPE_CHECKING:

    from . import float



class Point2i(_GraphWrapper):
    """A point with an x and y as ints"""

    def execute(self, context):

        return self._inner.execute(context)


    def distance(self, rhs) -> float.Float:
        """Point 2 Int Distance

        The Euclidean distance between two Point 2 Ints, returned as a Float.
    
        Args:
            rhs: Graph of Point2i
            
    
        Returns:
            Graph: A graph node producing a Float.
        """
        lhs_parsed = input_parsers.parse_graph(self)
        rhs_parsed = input_parsers.parse_graph(rhs)
        result = _internal.point2i_distance_internal(lhs_parsed, rhs_parsed)

        from .float import Float
        return Float(result)

    @staticmethod
    def from_components(x, y) -> Point2i:
        """Point 2 Int from Components

        Given an x and y creates a point
    
        Args:
            x: Graph of Int
            y: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Point2i.
        """
        x_parsed = input_parsers.parse_int_graph(x)
        y_parsed = input_parsers.parse_int_graph(y)
        result = _internal.point2i_from_components_internal(x_parsed, y_parsed)

        return Point2i(result)

